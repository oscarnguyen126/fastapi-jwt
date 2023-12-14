from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title" : "first title",
                "content": "first content"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "fullname": "Bek",
                "email": "help@bekbrace.com",
                "password": "123"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "email": "help@bekbrace.com",
                "password": "123"
            }
        }