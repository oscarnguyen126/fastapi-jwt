import uvicorn
from fastapi import FastAPI, Body, Depends
from fastapi.responses import JSONResponse
from models import PostSchema, UserLoginSchema, UserSchema
from jwt_handler import signJWT
from jwt_bearer import jwtBearer


posts = [
    {
        "id": 1,
        "title": "penguins",
        "content": "Penguins are a group of aquatic flightless birds."
    },
        {
        "id": 2,
        "title": "tigers",
        "content": "Tigers are the largest living cat species"
    },
        {
        "id": 3,
        "title": "koalas",
        "content": "Koala is arboreal herbivorous marsupial native to Australia."
    }
]

users = []


app = FastAPI()

@app.get('/')
def health_check():
    return JSONResponse(content={"status": "Running!"})


@app.get("/posts", dependencies=[Depends(jwtBearer())])
def get_posts():
    return {"data": posts}


@app.get("/posts/{id}", dependencies=[Depends(jwtBearer())])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "Post with this ID does not exists"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts")
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post Added!"
    }


@app.post("/user/signup")
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login")
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details!"
        }