from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Nick"},
    {"id": 2, "role": "moderator", "name": "Anna"},
    {"id": 3, "role": "user", "name": "John", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00.0000", "type_degree": "expert"}
    ]}
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 321, "amount": 2.12},
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "sell": 321, "amount": 2.12}
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def get_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


@app.get("/trades/user/{user_id}")
def get_trades_by_user(user_id: int):
    return [trade for trade in fake_trades if trade.get("user_id") == user_id]
