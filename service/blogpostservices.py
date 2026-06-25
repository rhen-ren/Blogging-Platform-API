from dependency import run_db
from schema.post import CreatePost, GetPost
from model.post import Post, Category
from sqlalchemy import select
from sqlalchemy.orm import Session

def create_post(post: CreatePost, db: Session):
    # check if category exists
    query = select(Category).where(Category.category_title == post.category)
    is_category_exists: Category = db.execute(query).scalar_one_or_none()

    newPost = None

    if is_category_exists:
        newPost = Post(
            title = post.title,
            content = post.content,
            category_id = is_category_exists.id
        )
        db.add(newPost)
        db.commit()

    elif not is_category_exists:
        is_category_exists = Category(
            category_title = post.category
        )
        db.add(is_category_exists)
        db.commit()
        db.refresh(is_category_exists)

        newPost = Post(
            title = post.title,
            content = post.content,
            category_id = is_category_exists.id
        )
        db.add(newPost)
        db.commit()

    return GetPost(
        id = newPost.id,
        content = newPost.content,
        category = is_category_exists.category_title,
        category_id = newPost.category_id
    )



