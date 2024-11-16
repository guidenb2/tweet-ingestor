#!/bin/bash

/opt/bitnami/kafka/bin/kafka-topics.sh --create --topic "$INPUT_TOPIC_NAME" --bootstrap-server kafka:9092 --partitions "$PARTITIONS" --replication-factor "$REPLICATION_FACTOR"
/opt/bitnami/kafka/bin/kafka-topics.sh --create --topic "$OUTPUT_TOPIC_NAME" --bootstrap-server kafka:9092 --partitions "$PARTITIONS" --replication-factor "$REPLICATION_FACTOR"
