from flask_app.config.mysqlconnection import  connectToMySQL
#from flask import flash

class Movie:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.genre = data['genre']
        self.plot = data['plot']
        self.liked = data['liked']
        self.disliked = data['disliked']
        self.favorited = data['favorited']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #self.user_id = data['user_id']

    @classmethod
    def save_interaction(cls, formulario):
        query = "INSERT INTO interactions (comment, liked, disliked, favorited, user_id, movie_id) VALUES (%(comment)s, %(liked)s, %(disliked)s, %(favorited)s, %(user_id)s, %(movie_id)s);"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        return result
    
    @classmethod
    def get_by_id(cls, formulario_movie):
        query = "SELECT * FROM movies WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario_movie)
        movie = cls(result[0])
        return movie

    @classmethod
    def like(cls, formulario_movie):
        query = "UPDATE movies SET liked = liked + 1  WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario_movie)
        query_2 = "SELECT * FROM movies WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query_2, formulario_movie)
        movie = cls(result[0])
        return movie
    
    @classmethod
    def dislike(cls, formulario_movie):
        query = "UPDATE movies SET disliked = disliked + 1  WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario_movie)
        query_2 = "SELECT * FROM movies WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query_2, formulario_movie)
        movie = cls(result[0])
        return movie

    @classmethod
    def favorite(cls, formulario_movie):
        query = "UPDATE movies SET favorited = favorited + 1  WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario_movie)
        query_2 = "SELECT * FROM movies WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query_2, formulario_movie)
        movie = cls(result[0])
        return movie
    
    @classmethod
    def get_all_liked(cls, formulario):
        query = "SELECT users.id, interactions.liked, interactions.movie_id FROM users LEFT JOIN interactions ON users.id = interactions.user_id WHERE users.id = %(id)s;"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        #movie_ids = result[0]['liked']
        #movie_ids = []
        #for movie_id in result:
        #    movie_ids.append(movie_id)
        #return movie_ids
        return result

    @classmethod
    def get_all_disliked(cls, formulario):
        query = "SELECT users.id, interactions.disliked, interactions.movie_id FROM users LEFT JOIN interactions ON users.id = interactions.user_id WHERE users.id = %(id)s;"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        return result

    @classmethod
    def get_all_favorited(cls, formulario):
        query = "SELECT users.id, interactions.favorited, interactions.movie_id FROM users LEFT JOIN interactions ON users.id = interactions.user_id WHERE users.id = %(id)s;"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        return result