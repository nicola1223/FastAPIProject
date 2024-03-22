from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Nick"},
    {"id": 2, "role": "moderator", "name": "Anna"},
    {"id": 3, "role": "user", "name": "John"}
]


class User(BaseModel):
    id: int
    role: str
    name: str


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
