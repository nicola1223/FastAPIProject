from fastapi import FastAPI

app = FastAPI(
    title="App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Nick"},
    {"id": 2, "role": "moderator", "name": "Anna"},
    {"id": 3, "role": "user", "name": "John"}
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 321, "amount": 2.12},
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "sell": 321, "amount": 2.12}
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
