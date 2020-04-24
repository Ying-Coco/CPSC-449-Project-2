# CPSC-449-Project-1

# Support Contacts

|        | Team           | Contact Info                   | Runbook Review                  |
|--------|----------------|--------------------------------|---------------------------------|
|Level 1 | Dev            | bobberino98@csu.fullerton.edu  | James Dobson - 4/23/2020        |
|Level 2 | SDET           | ywen1306@csu.fullerton.edu     | Yinglin Wen - 4/23/2020         |
|Level 3 | Operation      | almuhana@csu.fullerton.edu     | Abdulmalik Almuhana - 4/23/2020 |


# Requirements

User's system must have installed: Flask v1.1.1, Caddy v1.0.4, and Gunicorn v20.0.4.
For the test suite, the system must also have faker, locust, pytest, and tavern installed.
If these requirements are not available, a shell script (setup.sh) is provided that will install them for the user. To run the setup enter the command: 

bash setup.sh

# Starting the Services
To start the services, these commands must be run, in separate terminals, from the base directory:

ulimit -n 8192 && caddy

foreman start -m posts=3,accounts=3

There is a shell script (start_server.sh) that will run these commands automatically, opening terimnals for each server

# Shutting down the Services
To shut down the servers, simply kill the processes in the terminal by either closing the windows or pressing Ctrl+C.


# Running the Test Suite
To run a basic test of all of the functionalities of the services, go to the test suite directory and run the basic_test.sh file with:

bash basic_test.sh

To run a load test using Locust, enter the command:

locust -f load_test.py --host=http://localhost:2015

Or run the shell script with:

bash load_test.sh

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



