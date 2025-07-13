#!/bin/bash

# POST a new timeline post
POST_RESPONSE=$(curl -s -X POST http://localhost:5000/api/timeline_post \
  -d "name=Harsh Shah" \
  -d "email=test@example.com" \
  -d "content=This is a test post from curl")

POST_ID=$(echo "$POST_RESPONSE" | grep -o '"id":[0-9]*' | cut -d':' -f2)

# Get all posts
curl -s http://localhost:5000/api/timeline_post

# Delete the test post
curl -s -X DELETE http://localhost:5000/api/timeline_post/$POST_ID