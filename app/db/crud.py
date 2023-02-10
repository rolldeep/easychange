from sqlalchemy.orm import Session

from . import models

from app.model import schemas


def get_pair_by_name(db: Session, name: str):
    return db.query(models.Pair).filter(models.Pair.name == name).first()


def get_pairs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pair).offset(skip).limit(limit).all()

