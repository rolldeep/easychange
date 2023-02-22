from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.model.schemas import Pair
from app.db import crud
import uvicorn
from app.db.database import SessionLocal, engine, get_db


app = FastAPI()


@app.get("/pairs/", response_model=List[Pair])
def read_pairs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_pairs(db, skip=skip, limit=limit)
    return items


@app.get("/pairs/{name}", response_model=Pair)
def read_pair(name: str, db: Session = Depends(get_db)):
    db_pair = crud.get_pair(db=db, name=name)
    if db_pair is None:
        raise HTTPException(status_code=404, detail="Pair not found")
    return db_pair

@app.get("/", response_model=List[Pair])
def get_home(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_pairs(db, skip=skip, limit=limit)
    return items


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
