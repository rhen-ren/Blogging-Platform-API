from dependency import run_db
from schema.post import CreatePost, GetPost
from model.post import Post
from model.category import Category
from model.tag import Tag
from model.posttags import PostTags
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def create_post(post: CreatePost, db: Session):
    try:
        category = db.execute(select(Category).where(Category.category_title == post.category)).scalar_one_or_none()
        tags = db.execute(select(Tag).where(Tag.tag_title.in_(post.tags))).scalars().all()

        existingTagTitle: list = [tag.tag_title for tag in tags]
        currentTagIds: list = [tag.id for tag in tags]
        currentCategoryId: int  = 0

        #if tagsExist
        for postTag in post.tags:
            if postTag not in existingTagTitle:
                #create tag
                newTag = Tag(
                    tag_title = postTag
                )
                db.add(newTag)
                db.flush()
                currentTagIds.append(newTag.id)

        #if categoryExist
        if category:
            if post.category == category.category_title:
                currentCategoryId = category.id
        elif not category:
                #create category
                newCategory = Category(
                    category_title = post.category
                )
                db.add(newCategory)
                db.flush()
                currentCategoryId = newCategory.id
            
        #create post
        newPost = Post(
           title = post.title,
           content = post.content,
           category_id = currentCategoryId
        )

        db.add(newPost)
        db.flush()

        #create post tag link
        for tagId in currentTagIds:
            newLink = PostTags(
                post_id = newPost.id,
                tag_id = tagId
            )
            db.add(newLink)
        db.commit()

        return JSONResponse(
            status_code=201,
            content={"message": "Success"}
        )

    except Exception as e:
        db.rollback()
        raise e

def update_post(post: CreatePost, post_id: int, db:Session):
    try:
        tags = db.execute(select(Tag).where(Tag.tag_title.in_(post.tags))).scalars().all()
        category = db.execute(select(Category).where(post.category == Category.category_title)).scalars().one_or_none()
        existingTagTitle: list = [tag.tag_title for tag in tags]
        tagsId: list = [tag.id for tag in tags]
        postCategoryId: int = 0

        #updateCategory
        if category:
            postCategoryId = category.id
        elif not category:
            newCategory = Category(
                category_title = post.category
            )
            db.add(newCategory)
            db.flush()
            postCategoryId = newCategory.id

        #updateTags
        for postTag in post.tags:
            if postTag not in existingTagTitle:
                #create tag
                newTag = Tag(
                    tag_title = postTag
                )
                db.add(newTag)
                db.flush()
                tagsId.append(newTag.id)

        #updatePost
        query = (
            update(Post)
            .where(Post.id == post_id)
            .values(title = post.title, content = post.content, category_id = postCategoryId)
        )
        db.execute(query)
        db.flush()

        #updateTagsLinks
        db.execute(delete(PostTags).where(PostTags.post_id == post_id))
        db.flush()
        for tagId in tagsId:
            newLink = PostTags(
                post_id = post_id,
                tag_id = tagId
            )
            db.add(newLink)
        db.commit()
    except Exception as e:
        raise e




