# CPSC-449-Project-1

# Support Contacts

|        | Team           | Contact Info                   | Runbook Review                  |
|--------|----------------|--------------------------------|---------------------------------|
|Level 1 | Dev            | bobberino98@csu.fullerton.edu  | James Dobson - 4/23/2020        |
|Level 2 | SDET           | ywen1306@csu.fullerton.edu     | Yinglin Wen - 4/23/2020         |
|Level 3 | Operation      | almuhana@csu.fullerton.edu     | Abdulmalik Almuhana - 4/23/2020 |

 
# Requirements

**NB:** Ensure you have Python v3.6.7 or higher installed in your system.
In addition, the user's system must have the following installed: 
* flask v1.1.2
* caddy v1.0.4 (or higher)
* gunicorn v19.9.0 (or higher)
* Faker v4.0.3
* Locust v0.14.5
* pytest v5.4.1
* tavern v1.0.0

If these requirements are not available, a shell script (setup.sh) is provided that will install them for the user. To run the setup enter the command: 
```
    bash setup.sh
```


# Starting the Services
To start the services, these commands must be run, in separate terminals, from the base directory:

```
    ulimit -n 8192 && caddy

    foreman start -m posts=3,accounts=3,msgs=3,votes=3
```

There is a shell script (start_server.sh) that will run these commands automatically, opening terimnals for each server

# Shutting down the Services
To shut down the servers, simply kill the processes in the terminal by either closing the windows or pressing Ctrl+C.


# Running the Test Suite
To run a basic test of all of the functionalities of the services, **go to the test suite directory** and run the basic_test.sh file with:

```
    bash basic_test.sh
```

To run a load test using Locust, enter the command:

```
    locust -f load_test.py --host=http://localhost:2015
```

Or run the shell script with:

```
    bash load_test.sh
```

After staring the locust server, go to http://localhost:8089, enter your desired # of simulated users, the rate at which you want to hatch new users, and press start. when you are done, press stop to end the test and view the results.


# Network

| Service      | Port        | Protocol       |
|--------------|-------------|----------------|
| posts        | 5000        | TCP - http     |
| accounts     | 5100        | TCP - http     |
| msgs         | 5200        | TCP - http     |
| votes        | 5300        | TCP - http     |

# Filesystem

| Service          | Data                                       |
|------------------|--------------------------------------------|
| Posts            | /Deployment/PostAPI                        |
| Accounts         | /Deployment/UserAccountAPI                 |
| Post Database    | /Deployment/PostAPI/posts.db               |
| Account Database | /Deployment/UserAccountAPI/user_account.db |

# Routes
All routes should be accessed via http://localhost:2015

## Messages Service

| Endpoint | Request Type | Funcionality | Parameters (if any) |
| -------- | ------------ | ------------ | ------------------- |
| /msgs    | **GET**  | Show welcome Message |      |
| /msgs/send_msg | **POST** | Sends a message | *user_fr* (sender's username), *user_to* (receiver's username), *msg_desc* (body of message) |
| /msgs/delete_msg | **DELETE** | Deletes a message | *msg_id* (message id) |
| /msgs/fav_msg | **POST** | Mark a message as a favorite | *msg_id* (message id) |
| /msgs/unfav_msgs | **POST** | Mark a message as unfavorite | *msg_id* (message id) |

## Posts Service

| Endpoint | Request Type | Functionality | Parameters (if any) |
| -------- | ------------ | ------------- | ------------------- |
| /posts | **GET** | Show hello message | |
| /posts/create-post | **PUT** | Creates a post | *title* , *text* , *community* , *URL* , *username* , *postDate* |
| /posts/delete | **DELETE** | Deletes a post | *title* |
| /posts/retrieve | **GET** | Retrieves a post | *title* |
| /posts/list-n-particular | **GET** | Lists n particular posts | *community* , *n* (number of posts) |
| /posts/list-recent | **GET** | Lists the most recent n posts | *n* (number of posts) |


## User Account Service

| Endpoint | Request Type | Functionality | Parameters (if any) |
| -------- | ------------ | ------------- | ------------------- |
| /accounts | **GET** | Shows user account service message | |
| /accounts/create-user | **PUT** | Creates a user account | *user_name* ,*email* , *karma* |
| /accounts/update-email | **POST** | Updates email of user | *user_name* , *email* |
| /accounts/increment-karma | **POST** | Increments a user's karma by 1 | *user_name* |
| /accounts/decrement-karma | **POST** | Decrements a user's karma by 1 | *user_name* |
| /accounts/deactivate-account | **DELETE** | Deactivates account of user | *user_name* |

## Voting Service

| Endpoint | Request Type | Functionality | Parameters (if any) |
| -------- | ------------ | ------------- | ------------------- |
| /votes | **GET** | Shows Hello message | |
| /votes/up_vote | **POST** | Adds vote count by 1 | *pID* (post ID) |
| /votes/down_vote | **POST** | Decreases vote count by 1 | *pID* (post ID) |
| /votes/retrieve_votes | **GET** | Retrieves votes for a post | *pID* (post ID) |
| /votes/list_top_posts_byvotes | **GET** | Lists top posts by vote count | *n* (number of posts) |
| /votes/get_list | **GET** | Gets list of votes in a post | *title* |