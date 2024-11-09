from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    screen_name: str

class Coordinates(BaseModel):
    latitude: float
    longitude: float

class Tweet(BaseModel):
    created_at: str
    id: int
    full_text: str
    user: User
    retweet_count: int
    favourite_count: int
    lang: str
    is_retweet: bool
    geo: Optional[str]
    coordinates: Optional[Coordinates]
    place: Optional[str]

app=FastAPI()

@app.post("/")
def ingest_tweet(tweet: Tweet):
    return {"Message": "Hello world"}
