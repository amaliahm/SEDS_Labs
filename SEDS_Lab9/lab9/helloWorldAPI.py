#!/usr/bin/python3

from fastapi import FastAPI

# install fastAPI object
app = FastAPI()

# get endpoit
@app.get("/")

async def hello_world():
  return { "hello": "world" }
# async method returning json response
