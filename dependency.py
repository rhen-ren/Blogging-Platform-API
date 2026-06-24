from db import sessionLocal

def run_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
