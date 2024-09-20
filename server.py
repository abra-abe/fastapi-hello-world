from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/name")
def names():
    return {"name": "Abraham"}


# creating a dictionary to be used
users = {
    1: {
        "name": "Abraham",
        "age": 24,
        "occupation": "developer"
    },
    2: {
        "name": "Greg",
        "age": 24,
        "occupation": "Defensive security"
    },
    3: {
        "name": "Sam",
        "age": 24,
        "occupation": "offensive security"
    }
}

# user class
class User(BaseModel):
    name: str
    age: int
    occupation: str

# user class for updating
class UserUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int] 
    occupation: Optional[str] 

# Route parameters
@app.get("/user/{user_id}")
def get_users(user_id: int = Path(description="Enter the user ID")):
    return users[user_id]


# query parameters
@app.get("/search-user")
def search_users(user_name: str = ""):
    for user_id in users:
        if users[user_id]["name"] == user_name:
            return users[user_id]
        return {"message": "Data not found"}
    

# Combining route and query parameters
@app.get("/user_details/{user_id}")
def user_details(user_id: int, user_age: int = 24):
    # user_occupation = users[user_id]["age"]
    if users[user_id]["age"] == user_age:
        return {"occupation": users[user_id]["occupation"]}
    return {"message": "Data not found"}


# Post Methods

@app.post("/add-user")
def create_user(user_id: int, user: User):
    if user_id in users:
        return {"error": "User with id: "+str(user_id)+" already exists"}
    
    users[user_id] = user
    return users

# Put methods
@app.put("/update-user")
def update_user(user_id: int, user: UserUpdate):
    if user_id not in users:
        return {"error": f"User with id: {user_id} does not exist"}

    # Access the existing user dictionary
    existing_user = users[user_id]

    # Update only the fields that are provided (i.e., not None)
    if user.name is not None:
        existing_user["name"] = user.name

    if user.age is not None:
        existing_user["age"] = user.age

    if user.occupation is not None:
        existing_user["occupation"] = user.occupation

    # Return the updated user
    return existing_user

# testing something
@app.get("/users")
def get_users():
    return users

