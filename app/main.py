from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()





while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastAPI', user = 'postgres', password = 'rsadnan020626', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database Connected")
        break
    except Exception as error:
        print("Connection to Database failed")
        print("Error", error)
        time.sleep(2)

my_posts = [{"title" : "The Dark Knight", "content" : "Batman and the Joker", "id" : 1},
            {"title" : "The Long Halloween", "content" : "Batman and Carmine Falcone", "id" : 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


#request Get method url : /
@app.get("/")
def root():
    return {"message": "Welcome to API"}





