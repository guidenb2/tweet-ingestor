from prometheus_fastapi_instrumentator import Instrumentator 
from fastapi import FastAPI, HTTPException
from app.models import Tweet
from app.kafka import acked, init_producer
from app.config import read_config


app=FastAPI()
Instrumentator().instrument(app).expose(app)
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
