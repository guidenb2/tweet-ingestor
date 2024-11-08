#!/bin/bash

curl -X POST "http://0.0.0.0:8001/" \
    -H "Content-Type: application/json" \
    -d '{
        "created_at": "Mon Oct 21 19:00:00 +0000 2024",
        "id": 12345,
        "full_text": "All That Was East Is West Of Me Now was released 1 year ago this week!",
        "user": {
            "id": 8894744,
            "name": "Glen Hansard",
            "screen_name": "Glen_Hansard"
        },
        "retweet_count": 6,
        "favourite_count": 95,
        "lang": "en",
        "is_retweet": false,
        "geo": null,
        "coordinates": null,
        "place": null
    }'