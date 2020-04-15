import sqlite3
from flask import jsonify

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('service.db', isolation_level=None)
        self.create_vote_table()

    def create_vote_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "votes"(
            username TEXT,
            karma INTEGER,
            title TEXT,
            up_vote INTEGER,
            down_vote INTEGER
        );
        """
        self.conn.execute(query)

class VoteModel:
    def __init__(self):
        self.conn = sqlite3.connect('service.db', isolation_level=None)
        self.table_name = 'Vote'
    

    def up_vote(self, title):
        query = 'UPDATE {self.table_name} SET up_vote = up_vote + 1 WHERE title = "{title}"'
        try:
            self.conn.execute(query)
            return {'message': 'Upvote success.'}
            self.conn.commit()
        except:
            return {'message':'Could not upvote for {title} you entered!'}

    def down_vote(self, title):
        query = 'UPDATE {self.table_name} SET down_vote = down_vote + 1 WHERE title = "{title}"'
        try:
            self.conn.execute(query)
            return {'message': 'Downvote for {title} is updated!'}
            self.conn.commit()
        except:
            return {'message':'Could not downvote for {title} you entered!'}


    def retrieve_votes(self, title):
        query = 'SELECT up_vote, down_vote FROM Vote INNER JOIN post Vote.title = Post.title WHERE title = ?'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
            
    def list_top_posts_byvotes(self, n):
        query = 'SELECT post.title FROM post INNER JOIN vote on post.title = vote.title ORDER BY abs(up_vote - down_vote) DESC LIMIT ?'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))

    def get_list(self, title):
        query = 'SELECT vote.title, up_vote, down_vote FROM post INNER JOIN vote on post.title = vote.title WHERE post.title LIKE {title}' \
                'ORDER BY (up_vote - down_vote) DESC;'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
