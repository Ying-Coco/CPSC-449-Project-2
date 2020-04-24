#!/bin/bash

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @./Data/message.json \
     http://localhost:5000/msgs/send_msg


curl --verbose \
     -X DELETE \
     --header 'Content-Type: application/json' \
     --data @./Data/delete.json \
     http://localhost:5000/msgs/delete_msg

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @./Data/fav.json \
     http://localhost:5000/msgs/fav_msg

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @./Data/unfav.json \
     http://localhost:5000/msgs/unfav_msg

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @./Data/upvote.json \
     http://localhost:5000/votes/up_vote


curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @./Data/downvote.json \
     http://localhost:5000/votes/down_vote

curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @./Data/retrieve.json \
     http://localhost:5000/votes/retrieve_votes

curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @./Data/topvotes.json \
     http://localhost:5000/votes/list_top_posts_byvotes

curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @./Data/getList.json \
     http://localhost:5000/votes/get_list