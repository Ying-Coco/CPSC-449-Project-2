import sqlite3
from flask import jsonify, abort

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        self.create_msg_table()

    def create_msg_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "messages"(
            msg_id INTEGER PRIMARY KEY NOT NULL,
            user_fr VARCHAR,
            user_to VARCHAR,
            msg_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            msg_desc TEXT,
            msg_flag VARCHAR,
            msg_favorite VARCHAR
        );
        """
        self.conn.execute(query)

class MsgModel:
    def __init__(self):
        self.table_name = "messages"

#curl -i -X POST -H 'Content-Type:application/json' -d 
    def send_msg(self, user_fr, user_to, msg_desc, msg_flag):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f"INSERT INTO messages (user_fr, user_to, msg_desc, msg_flag) VALUES ({user_fr}, {user_to}, {msg_desc}, {msg_flag})"
        try: 
            self.conn.execute(query)
            return {'message:' f'Message from {user_fr} to {user_fr} has been send.'}
            self.conn.commit()
        except:
            return {'message': f'Could not send message to {user_to}!'}
        self.conn.close()


#curl -i -X DELETE http://localhose:2015/msgs/delete_msg?msg_id=4
    def delete_msg(self, msg_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'DELETE FROM messages WHERE msg_id={msg_id}'
        try:
            self.conn.execute(query)
            return {'message': f'Message {msg_id} from message has been deleted.'}
            self.conn.commit()
        except:
            return {'message': f'Message {msg_id} cannot be deleted.'}
        self.conn.close()


#curl -i -X POST -H 'Content-Type:application/json' http://localhose:2015/msgs/fav_msg?msg_id=1
    def fav_msg(self, msg_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'UPDATE messages SET msg_favorite = Y WHERE msg_id={msg_id}'
        try:
            self.conn.execute(query)
            return {'message': f'Message {msg_id} has been favorited'}
            self.conn.commit()
        except:
            return {'message': f'Message {msg_id} cannot be favorited.'}
        self.conn.close()

    def unfav_msg(self, msg_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'UPDATE messages SET msg_favorite = N WHERE msg_id={msg_id}'
        try:
            self.conn.execute(query)
            return {'message': f'Message {msg_id} has been unfavorited.'}
            self.conn.commit()
        except:
            return {'message': f'Message {msg_id} cannot be unfavorited.'}
        self.conn.close()
