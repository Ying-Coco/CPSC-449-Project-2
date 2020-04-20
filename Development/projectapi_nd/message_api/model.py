import sqlite3
from flask import jsonify, abort
import json

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
            msg_flag BIT NOT NULL DEFAULT 0,
            FOREIGN KEY (user_fr) REFERENCES user(username),
            FOREIGN KEY (user_to) REFERENCES user(username)
        );
        """
        self.conn.execute(query)

class MsgModel:
    def __init__(self):
        self.table_name = "messages"

#curl -i -X POST -H 'Content-Type:application/json' -d 
    def send_msg(self, user_fr, user_to, msg_desc):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not user_fr or not user_to:
            return {"status_code": "409", "message": "Sender and/or receiver not entered!"}

        cursor = self.conn.cursor()
        query = f"SELECT username FROM User WHERE username='%s'" % (user_fr)    
        cursor.execute(query)
        user_fr = cursor.fetchone()
        #cursor.execute(f'SELECT username FROM User WHERE username = "{user_to}"')
        query = f"SELECT username FROM User WHERE username='%s'" % (user_to)  
        cursor.execute(query)
        user_to = cursor.fetchone()


        if not user_fr:
            return {'message': "user not found"}
        if not user_to:
            return {'message': "user not found"}

        string = ("INSERT INTO messages (user_fr, user_to, msg_desc) VALUES ('%s', '%s', '%s')" % (user_fr[0], user_to[0], msg_desc))
            

        try:
            query = cursor.execute(string)
            return {'message': f'Message from {user_fr[0]} to {user_to[0]} has been sent.'}
            self.conn.commit()
        except:
            print(query)
            return {'message': string}
        self.conn.close()



#curl -i -X DELETE http://localhose:2015/msgs/delete_msg?msg_id=4
    def delete_msg(self, msg_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not msg_id:
            return {'message': f'Please provide a message id.'}
        
        id_check = self.conn.execute('SELECT * FROM messages WHERE msg_id= ?', (msg_id,)).fetchall()
        if id_check != None:

            try:
                query = f'DELETE FROM messages WHERE msg_id={msg_id}'
                self.conn.execute(query)
                return {'message': f'Message {msg_id} from message has been deleted.'}
                self.conn.commit()
            except:
                return {'message': f'Message {msg_id} cannot be deleted.'}
        else:
            return {'message': f'Message not found!'}            
        self.conn.close()


#curl -i -X POST -H 'Content-Type:application/json' http://localhose:2015/msgs/fav_msg?msg_id=1
    def fav_msg(self, msg_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not msg_id:
            return {'message': f'Please provide a message id.'}
        
        id_check = self.conn.execute('SELECT * FROM messages WHERE msg_id= ?', (msg_id,)).fetchall()
        if id_check != None:
            try:
                query = f'UPDATE messages SET msg_flag = 1 WHERE msg_id={msg_id}'
                self.conn.execute(query)
                return {'message': f'Message {msg_id} has been favorited'}
                self.conn.commit()
            except:
                return {'message': f'Message {msg_id} cannot be favorited.'}
        else:
            return {'message': f'Message not found!'}
            
        self.conn.close()

    def unfav_msg(self, msg_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not msg_id:
            return {'message': f'Please provide a message id.'}
        
        id_check = self.conn.execute('SELECT * FROM messages WHERE msg_id= ?', (msg_id,)).fetchall()
        if id_check != None:
            try:
                query = f'UPDATE messages SET msg_flag = 0 WHERE msg_id={msg_id}'
                self.conn.execute(query)
                return {'message': f'Message {msg_id} has been unfavorited.'}
                self.conn.commit()
            except:
                return {'message': f'Message {msg_id} cannot be unfavorited.'} 
        else:
            return {'message': f'Message ID not found!'}
           
        self.conn.close()