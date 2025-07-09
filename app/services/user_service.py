from sqlalchemy.orm import Session
from app.db import models
from app.core.security import verify_password, get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models.user.User).filter(models.user.User.email == email).first()

def create_user(db: Session, email: str, password: str):
    hashed_pw = get_password_hash(password)
    user = models.user.User(email=email, password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
