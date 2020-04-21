from locust import HttpLocust, TaskSet, task, between
import json
import requests
from faker import Faker
from faker.providers import internet

fake = Faker()

# posting
community_list = [
    'hotpot', 'slushies', 'icee',
    'csuf', 'popmusic', 'dummies',
    'youtube', 'candy', 'pie',
    'pancake', 'Popular', 'fans', 'cereals'
]
title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
text = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
username = fake.user_name()
message = fake.sentence()
username2 = fake.user_name()
url = fake.image_url()
community = fake.word(ext_word_list=community_list)
n = fake.random_int(min=1, max=200,step=1)
postDate = fake.date()
msgID = fake.random_int(min=1, max=100, step=1)
postID = fake.random_int(min=1, max=100, step=1)
dataPost = {"title": title, "text": text,
            "username": username, "community": community, "URL": url, "postDate": postDate}
dataTitle = {"title": title}
dataListRecent = {"n": n}
dataListParticular = { "community": community,"n": n}

dataMsg = {"user_fr": username, "user_to": username2, "msg_desc": message}
# accounts
email = fake.email()
karma = fake.random_int(min=1, max=1000,step=1)

dataCreateUser = {"user_name": username, "email": email, "karma": karma}
dataUsername = {"user_name": username}
dataUsername2 = {"user_name": username2}
dataEmail = {"user_name": username, "email": email}
dataID = {"msg_id": msgID}
dataPID = {"pID": postID}
dataN = {"n": n}
dataList = {"title": "%e%"}


class userTask(TaskSet):

    @task(1)
    def post(self):
        self.client.put("/posts/create-post", json=dataPost)

    @task(2)
    def retrievePost(self):
        self.client.get("/posts/retrieve", json=dataTitle)

    @task(4)
    def deletePost(self):
        self.client.delete("/posts/delete", json=dataTitle)  # title

    @task(4)
    def listnParticularPost(self):
        self.client.get("/posts/list-n-particular", json=dataListParticular)  # community and n

    @task(2)
    def listRecentPost(self):
        self.client.get("/posts/list-recent", json=dataListRecent)  # n

    @task(1)
    def create_user(self):
        self.client.put("/accounts/create-user", json=dataCreateUser)

    @task(2)
    def update_email(self):
        self.client.post("/accounts/update-email", json=dataEmail)

    @task(3)
    def increment_karma(self):
        self.client.post("/accounts/increment-karma", json=dataUsername)

    @task(3)
    def decrement_karma(self):
        self.client.post("/accounts/decrement-karma", json=dataUsername)
    
    @task(3)
    def send_message(self): 
        self.client.post("/msgs/send_msg", json = dataMsg)
    
    @task(3)
    def fav_message(self): 
        self.client.post("/msgs/fav_msg", json = dataID)
    
    @task(4)
    def unfav_message(self): 
        self.client.post("/msgs/unfav_msg", json = dataID)
    
    @task(5)
    def delete_message(self): 
        self.client.delete("/msgs/delete_msg", json = dataID)
    
    @task(3)
    def up_vote(self): 
        self.client.post("/votes/up_vote", json = dataPID)
    
    @task(3)
    def down_vote(self): 
        self.client.post("/votes/down_vote", json = dataPID)
    
    @task(4)
    def retrieve_votes(self): 
        self.client.get("/votes/retrieve_votes", json = dataPID)
    
    @task(4)
    def list_top_posts_byvotes(self): 
        self.client.get("/votes/list_top_posts_byvotes", json = dataN)
    
    @task(4)
    def get_list(self): 
        self.client.get("/votes/get_list", json = dataList)

    @task(5)
    def deactivate_account(self):
        self.client.delete("/accounts/deactivate-account", json=dataUsername)



class websiteUser(HttpLocust):
    task_set = userTask
    wait_time = between(2000,5000)
    
