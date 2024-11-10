from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.kafka import acked, init_producer
from app.config import read_config

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
config = read_config()
producer = init_producer(config)

@app.post("/")
def ingest_tweet(tweet: Tweet):
    try:
        producer.produce("raw_tweets",
                         value=tweet.model_dump_json(),
                         callback=acked)
        producer.poll(1)
        return {"status": "success",
                "message": "Tweet added to kafka queue successfully"}
    except Exception as error:
        raise HTTPException(status_code=500,
                            detail={
                                "status": "error",
                                "message": "Failed to add tweet to kafka queue",
                                "error": str(error)
        })
