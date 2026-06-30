from dependency import run_db
from schema.post import CreatePost, GetPost
from model.post import Post
from model.category import Category
from model.tag import Tag
from model.posttags import PostTags
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def create_post(post: CreatePost, db: Session):
    try:
        category = db.execute(select(Category).where(Category.category_title == post.category)).scalar_one_or_none()
        tags = db.execute(select(Tag).where(Tag.tag_title.in_(post.tags))).scalars().all()

        existingTagTitle = [tag.tag_title for tag in tags]
        currentTagIds = [tag.id for tag in tags]
        currentCategoryId = 0

        #if tagsExist
        for postTag in post.tags:
            if postTag not in existingTagTitle:
                #create tag
                newTag = Tag(
                    tag_title = postTag
                )
                db.add(newTag)
                db.commit()
                db.refresh(newTag)
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
                db.commit()
                db.refresh(newCategory)
                currentCategoryId = newCategory.id
            
        #create post
        newPost = Post(
           title = post.title,
           content = post.content,
           category_id = currentCategoryId
        )

        db.add(newPost)
        db.commit()
        db.refresh(newPost)

        #create post tag link
        for tagId in currentTagIds:
            newLink = PostTags(
                post_id = newPost.id,
                tag_id = tagId
            )
            db.add(newLink)
        db.commit()

        db.close()
        return JSONResponse(
            status_code=201,
            content={"message": "Success"}
        )

    except Exception as e:
        db.rollback()
        raise e





