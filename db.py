from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///blogposts.db"

engine = create_engine(DATABASE_URL, echo=True)
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()