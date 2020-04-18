import sqlite3
from flask import jsonify

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        self.create_vote_table()

    def create_vote_table(self):

        query = """
        ALTER TABLE "Post"(
            vote_id INTEGER AUTO_INCREMENT UNIQUE NOT NULL,
            up_vote INTEGER,
            down_vote INTEGER
        );
        """
        #this keep giving me an error, see if it gives you an error
        #self.conn.execute(query)
        #sqlite3.OperationalError: near "(": syntax error
        

class VoteModel:
    def __init__(self):
        
        self.table_name = 'vote'
    
    #upvote example: curl -i 'http://localhost:2015/votes/up_vote?title=hello';
    def up_vote(self, vote_id):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'UPDATE votes SET up_vote = up_vote + 1 WHERE vote_id = "{vote_id}"'
        if not title:
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
        query = 'UPDATE votes SET down_vote = down_vote + 1 WHERE vote_id = "{vote_id}"'
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
        query = 'SELECT up_vote, down_vote FROM votes INNER JOIN post Vote.title = Post.title WHERE vote_id = ?'
        result = self.conn.execute(query).fetchall()
        if result:
            return jsonify(list(result))
        else:
            return{'message': f'No results found!'}
        self.conn.close()
    
    #list top post by votes example: curl -i 'http://localhost:2015/votes/list_top_posts_byvotes?n=5'
    def list_top_posts_byvotes(self, n):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'SELECT post.title FROM post INNER JOIN votes on post.title = votes.title ORDER BY abs(up_vote - down_vote) DESC LIMIT ?'
        result = self.conn.execute(query).fetchall()
        if result:
            return jsonify(list(result))
        else:
            return{'message': f'No results found!'}
        self.conn.close()

    #get list example: curl -i 'http://localhost:2015/votes/get_list?title=%t%'
    def get_list(self, title):
        self.conn = sqlite3.connect('../service.db', isolation_level=None)
        query = 'SELECT vote.title, up_vote, down_vote FROM post INNER JOIN votes on post.title = votes.title WHERE post.title LIKE %{title}%' \
                'ORDER BY (up_vote - down_vote) DESC;'
        result = self.conn.execute(query).fetchall()
        if result:
            return jsonify(list(result))
        else: 
            return {'message': f'No results found!'}
        self.conn.close()
