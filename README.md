# Blogging Platform API

A simple blogging platform API built using FastAPI and SQLAlchemy
## Features
- Create, delete, updated, and fetch blog posts.
- Associate posts with categories
- Tag posts with multiple tags
- Automatic creation of categories and tags if non existing
- JSON responses
## Tech Stack
- FastAPI
- SQLAlchemy ORM
- Pydantic
## Database Schema
- Post: post_id, title, content, category_id
- Category: category_id, category_name
- Tag: tag_id, tag_name
- PostTag: post_id, tag_id
<img width="911" height="152" alt="Blogging Platfrom ERD drawio" src="https://github.com/user-attachments/assets/b386d871-1086-48dd-b2cf-de81431569d0" />
##Roadmap Project
[Blogging Platform API Roadmap Project](https://roadmap.sh/projects/blogging-platform-api)
