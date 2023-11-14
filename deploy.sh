#!/bin/bash

cd /home/ubuntu/Desktop/3203test_scene1

echo "Stopping the containers..."
docker-compose down

echo "Buidling the containers..."
docker-compose up --build -d

echo "Containers up and running..."
