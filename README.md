# tweet-ingestor
Microservice for receiving tweets and storing them on a kafka topic

## Running the service
To run the service, run the script:
```
./scripts/run.sh
```

### Create a Kafka cluster
To start a kafka cluster, run the following command:
```
docker-compose up -d
```

### Sending a simple tweet
To send a simple tweet, execute the script:
```
./scripts/send-tweet.sh
```
