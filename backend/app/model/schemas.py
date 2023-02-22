
from pydantic import BaseModel


class Pair(BaseModel):
    id: int
    name: str
    datetime: str
    high: float
    low: float
    open: float
    close: float

    class Config:
        orm_mode = True

