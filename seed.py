from db import SessionLocal, init_db
from models import User

def seed_users():
    init_db()
    db = SessionLocal()
    if db.query(User).count() == 0:
        users = [
            User(name="Alice", email="alice@example.com"),
            User(name="Bob", email="bob@example.com"),
            User(name="Charlie", email="charlie@example.com"),
        ]
        db.add_all(users)
        db.commit()
    db.close()

if __name__ == "__main__":
    seed_users()
