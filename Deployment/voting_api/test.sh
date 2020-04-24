#!/bin/bash

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @upvote.json \
     http://127.0.0.1:5000/votes/up_vote


curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @downvote.json \
     http://127.0.0.1:5000/votes/down_vote

curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @retrieve.json \
     http://127.0.0.1:5000/votes/retrieve_votes

curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @topvotes.json \
     http://127.0.0.1:5000/votes/list_top_posts_byvotes

curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @getList.json \
     http://127.0.0.1:5000/votes/get_list