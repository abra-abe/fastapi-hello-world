from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/name")
def names():
    return {"name": "Abraham"}

# using route parameters
# creating a dictionary to be fetched
users = {
    1: {
        "name": "Abraham",
        "age": 24,
    },
    2: {
        "name": "Greg",
        "age": 24
    }
}

@app.get("/users/{user_id}")
def get_users(user_id: int):
    return users[user_id]