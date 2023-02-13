from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.model.schemas import Pair
from app.db import crud
from app.db.database import SessionLocal, engine, get_db


app = FastAPI()


@app.get("/pairs/", response_model=List[Pair])
def read_pairs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_pairs(db, skip=skip, limit=limit)
    return items


@app.get("/pairs/{pair_id}", response_model=Pair)
def read_user(pair_id: int, db: Session = Depends(get_db)):
    db_pair = crud.get_pair(db, pair_id=pair_id)
    if db_pair is None:
        raise HTTPException(status_code=404, detail="Pair not found")
    return db_pair

@app.get("/", response_model=List[Pair])
def get_home(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_pairs(db, skip=skip, limit=limit)
    return items