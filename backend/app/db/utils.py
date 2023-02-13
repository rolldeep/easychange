from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import csv
load_dotenv()

from models import Pair
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    for filename in os.listdir('data'):
        with open(f"data/{filename}", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            pairname = filename.split("-")[0]
            for row in reader:
                data = Pair(name=pairname, datetime=row['DATE_TIME'], 
                high=row['HIGH'], low=row['LOW'], open=row['OPEN'], close=row['CLOSE'])
                db.add(data)
        db.commit()

if __name__ == "__main__":
    init_db()
    print("Done")
