from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/name")
def names():
    return {"name": "Abraham"}

# using route parameters
# creating a dictionary to be used
users = {
    1: {
        "name": "Abraham",
        "age": 24,
    },
    2: {
        "name": "Greg",
        "age": 24
    },
    3: {
        "name": "Sam",
        "age": 24
    }
}

@app.get("/user/{user_id}")
def get_users(user_id: int = Path(description="Enter the user ID")):
    return users[user_id]

@app.get("/users/{user_id}")
def get_users(user_id: Optional[int] = None):
    return users[user_id]


# query parameters
@app.get("/search-user")
def search_users(user_name: str):
    for user_id in users:
        if users[user_id]["name"] == user_name:
            return users[user_id]
        return {"message": "Data not found"}