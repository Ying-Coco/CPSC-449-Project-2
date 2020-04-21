#!/bin/bash

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @message.json \
     http://127.0.0.1:5000/msgs/send_msg


curl --verbose \
     -X DELETE \
     --header 'Content-Type: application/json' \
     --data @delete.json \
     http://127.0.0.1:5000/msgs/delete_msg

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @fav.json \
     http://127.0.0.1:5000/msgs/fav_msg

curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @unfav.json \
     http://127.0.0.1:5000/msgs/unfav_msg