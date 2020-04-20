import sqlite3
from flask import jsonify

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)

class VoteModel:
    #upvote example: curl -i 'http://localhost:2015/votes/up_vote?vote_id=2';
    def up_vote(self, pID):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not pID:
            return {'message': f'Please provide a post id.'}
        id_check = self.conn.execute('SELECT * FROM Post WHERE pID = ?', (pID,)).fetchall()
        if id_check:
            try:
                query = f'UPDATE Post SET up_vote = (up_vote + 1) WHERE pID = "{pID}";'
                self.conn.execute(query)
                return {'message': 'Upvote success.'}
                self.conn.commit()
            except:
                return {'message':f'Could not upvote for {pID} you entered!'}
        else:
            return {'message': f'Post not found!'} 
        self.conn.close()


    #downvote example: curl -i 'http://localhost:2015/votes/down_vote?vote_id=2';
    def down_vote(self, pID):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not pID:
            return {'message': f'Please provide a post id.'}
        id_check = self.conn.execute('SELECT * FROM Post WHERE pID = ?', (pID,)).fetchall()
        if id_check:
            try:
                query = f'UPDATE Post SET down_vote = (down_vote + 1) WHERE pID = "{pID,}";'
                self.conn.execute(query)
                return {'message': f'Downvote for {pID} is updated!'}
                self.conn.commit()
            except:
                return {'message':f'Could not downvote for {pID} you entered!'}
        else:
            return {'message': f'Post not found!'}             
        self.conn.close()

    #retrieve votes example: curl -i 'http://localhost:2015/votes/retrieve_votes?vote_id=2';
    def retrieve_votes(self, pID):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        if not pID:
            return {'message': f'Please provide a post id.'}
        id_check = self.conn.execute('SELECT * FROM Post WHERE pID = ?', (pID,)).fetchall()
        if id_check:
            try: 
                query = f'SELECT abs(up_vote - down_vote) AS total_vote FROM Post WHERE pID = "{pID}";'
                result = self.conn.execute(query).fetchall()
                return jsonify(list(result))
            except:
                return {'message': 'Post not found!'}
        self.conn.close()
    
    #list top post by votes example: curl -i 'http://localhost:2015/votes/list_top_posts_byvotes?n=5'
    def list_top_posts_byvotes(self, n):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'SELECT title, abs(up_vote - down_vote) AS total_vote FROM Post ORDER BY abs(up_vote - down_vote) DESC;'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
        self.conn.close()

    #get list example: curl -i 'http://localhost:2015/votes/get_list?title=%te%'
    def get_list(self, title):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = f'SELECT title, abs(up_vote - down_vote) AS total_vote FROM Post WHERE title LIKE "{title}" ORDER BY (up_vote - down_vote) DESC;'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
        self.conn.close()