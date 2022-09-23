from flask_app.config.mysqlconnection import  connectToMySQL

class Interaction:

    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.liked = data['liked']
        self.disliked = data['disliked']
        self.liked = data['liked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']

    @classmethod
    def already_liked(cls, formulario):
        query = "SELECT liked FROM interactions WHERE user_id = %(user_id)s AND movie_id = %(movie_id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        len_result = len(result)
        return len_result

    @classmethod
    def already_disliked(cls, formulario):
        query = "SELECT disliked FROM interactions WHERE user_id = %(user_id)s AND movie_id = %(movie_id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        len_result = len(result)
        return len_result

    @classmethod
    def already_favorited(cls, formulario):
        query = "SELECT favorited FROM interactions WHERE user_id = %(user_id)s AND movie_id = %(movie_id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        len_result = len(result)
        return len_result

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM interactions WHERE user_id = %(id)s AND movie_id = %(movie_id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        interaction = cls(result[0])
        return interaction
