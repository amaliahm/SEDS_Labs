from pydantic import BaseModel
import datetime

class PostBase(BaseModel):
  publishedAt: datetime.datetime
  title: str
  content: str

class UserBase(BaseModel):
  name: str
  email: str
  
class Post(PostBase):
  id: int
  author: int
  class Config:
    from_attributes = True

class User(UserBase):
  id: int
  class Config:
    from_attributes = True
    
class PostCreate(PostBase):
  pass

class UserCreate(UserBase):
  posts: list[Post] = []
  pass
