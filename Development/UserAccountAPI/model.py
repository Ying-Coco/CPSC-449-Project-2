import sqlite3
from flask import jsonify
class Schema:
    def __init__(self):
        # connecting to the database
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        # table 
        self.create_user_table()

    def create_user_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "User" (
          username TEXT,
          email TEXT,
          karma INTEGER
        );
        """

        self.conn.execute(query)


class UserModel:
    def __init__(self):
        
        self.table_name = 'User'

    def create_user(self, user_name, email, karma):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'insert into {self.table_name} ' \
                f'(username, email, karma) ' \
                f'values ("{user_name}","{email}", "{karma}");'
        

        try:
            self.conn.execute(query)
            return {'message': f'User with the username: {user_name} is created!'}
            self.conn.commit()
        except:
            return {'message': 'Could not create the user!'}
        self.conn.close()
    
    def update_email(self, user_name, email):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'UPDATE {self.table_name} SET email = "{email}" WHERE username = "{user_name};"'
        try:
            self.conn.execute(query)
            return {'message': f'Email for {user_name} is updated!'}
            self.conn.commit()
        except:
            return {'message': f'Could not update the email for {user_name};'}
        self.conn.close()
    
    def increment_karma(self, user_name):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'UPDATE {self.table_name} SET karma = karma + 1 WHERE username = "{user_name}";'
        try:
            self.conn.execute(query)
            return {'message': f'Karma for {user_name} is incremented!'}
            self.conn.commit()
        except:
            return {'message': f'Could not increment the karma for {user_name}'}
        self.conn.close()
    
    def decrement_karma(self, user_name):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'UPDATE {self.table_name} SET karma = karma - 1 WHERE username = "{user_name}";'
        try:
            self.conn.execute(query)
            return {'message': f'Karma for {user_name} is decremented!'}
            self.conn.commit()
        except:
            return {'message': f'Could not decrement the karma for {user_name};'}
        self.conn.close()
    
    def deactivate_account(self, user_name):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'DELETE FROM {self.table_name} ' \
                f'WHERE username = "{user_name}";'
        try:
            self.conn.execute(query)
            return {'message': f'The account for {user_name} is deactivated!'}
            self.conn.commit()
        except:
            return {'message': f'Could not deactivate the account for {user_name}.'}
        self.conn.close()
    
