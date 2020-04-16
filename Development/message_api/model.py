import sqlite3
from flask import jsonify, abort

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('service.db', isolation_level=None)
        self.create_msg_table()

    def create_msg_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "messages"(
            msg_id INTEGER PRIMARY KEY,
            user_fr VARCHAR,
            user_to VARCHAR,
            msg_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            msg_desc TEXT,
            msg_flag VARCHAR,
            msg_favorite VARCHAR,
        );
        """
        self.conn.execute(query)

class MsgModel:
    def __init__(self):
        self.conn = sqlite3.connect('service.db', isolation_level=None)
        self.table_name = 'messages'

    def send_msg(self, user_fr, user_to, msg_desc, msg_flag):
        query = "INSERT INTO {self.table_name} (user_fr, user_to, msg_desc, msg_flag) VALUES ((SELECT username FROM users WHERE username=?), (SELECT username FROM users WHERE username=?), {msg_desc}, {msg_flag})"
        try: 
            self.conn.execute(query)
            return {'message:' 'Message from {user_fr} to {user_fr} has been send.'}
            self.conn.commit()
        except:
            return {'message': 'Could not send message to {user_to}!'}

    def delete_msg(self, msg_id):
        query = 'DELETE FROM messages WHERE msg_id="{msg_id}"'
        try:
            self.conn.execute(query)
            return {'message': 'Message {msg_id} from message has been deleted.'}
            self.conn.commit()
        except:
            return {'message': 'Message {msg_id} cannot be delete.'}

    def fav_msg(self, msg_id):
        query = 'UPDATE {self.table_name} SET msg_favorite = Y WHERE msg_id={msg_id}'
        try:
            self.conn.execute(query)
            return {'message': 'Message {msg_id} has been favorited'}
            self.conn.commit()
        except:
            return{'message': 'Message {msg_id} cannot be favorite.'}

    def close(self):
        self.conn.close()