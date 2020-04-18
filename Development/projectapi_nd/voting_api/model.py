import sqlite3
from flask import jsonify

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)

class VoteModel:
    
    #upvote example: curl -i 'http://localhost:2015/votes/up_vote?title=hello';
    def up_vote(self, vote_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'UPDATE Post SET up_vote = up_vote + 1 WHERE vote_id = "{vote_id}"'
        if not vote_id:
            return page_not_found(404)
        else:
            try:
                self.conn.execute(query)
                return {'message': 'Upvote success.'}
                self.conn.commit()
            except:
                return {'message':'Could not upvote for {vote_id} you entered!'}
            self.conn.close()


    #downvote example: curl -i 'http://localhost:2015/votes/down_vote?title=hello';
    def down_vote(self, vote_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'UPDATE Post SET down_vote = down_vote + 1 WHERE vote_id = "{vote_id}"'
        if not vote_id:
            return page_not_found(404)
        else:
            try:
                self.conn.execute(query)
                return {'message': 'Downvote for {vote_id} is updated!'}
                self.conn.commit()
            except:
                return {'message':'Could not downvote for {vote_id} you entered!'}
            self.conn.close()

    #retrieve votes example: curl -i 'http://localhost:2015/votes/retrieve_votes?title=hello';
    def retrieve_votes(self, vote_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'SELECT up_vote, down_vote FROM Post WHERE vote_id = ?'
        result = self.conn.execute(query).fetchall()
        if result:
            return jsonify(list(result))
        else:
            return{'message': f'No results found!'}
        self.conn.close()
    
    #list top post by votes example: curl -i 'http://localhost:2015/votes/list_top_posts_byvotes?n=5'
    def list_top_posts_byvotes(self, n):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'SELECT title FROM Post ORDER BY abs(up_vote - down_vote) DESC LIMIT ?'
        result = self.conn.execute(query).fetchall()
        if result:
            return jsonify(list(result))
        else:
            return{'message': f'No results found!'}
        self.conn.close()

    #get list example: curl -i 'http://localhost:2015/votes/get_list?title=%t%'
    def get_list(self, title):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'SELECT title, up_vote, down_vote FROM Post WHERE post.title LIKE %{title}% ORDER BY (up_vote - down_vote) DESC;'
        result = self.conn.execute(query).fetchall()
        if result:
            return jsonify(list(result))
        else: 
            return {'message': f'No results found!'}
        self.conn.close()