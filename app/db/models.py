from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


class Pair(Base):
    __tablename__ = "pairs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    datetime = Column(String)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    close = Column(Float)

    # owner = relationship("User", back_populates="items")