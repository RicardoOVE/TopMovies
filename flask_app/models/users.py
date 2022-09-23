from flask_app.config.mysqlconnection import connectToMySQL
from flask import jsonify
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$')

#from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.nickname = data['nickname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (name, nickname, email, password) VALUES (%(name)s, %(nickname)s, %(email)s, %(password)s)"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        return result 

    @staticmethod
    def validate_user(formulario):
        if (len(formulario['name'])) <3:
            js_message = 'Name must be at least 3 letters long'
            return js_message

        if len(formulario['nickname']) <3:
            js_message = 'Nickname must be at least 3 letters long'
            return js_message

        query = "SELECT * FROM users WHERE email = %(nickname)s"
        results = connectToMySQL('topmovies').query_db(query, formulario)
        if len(results) >= 1:
            js_message = 'nickname already taken'
            return js_message

        if not EMAIL_REGEX.match(formulario['email']):
            js_message = 'Invalid email'
            return js_message

        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('topmovies').query_db(query, formulario)
        if len(results) >= 1:
            js_message = 'email already registred'
            return js_message

        if not PASSWORD_REGEX.match(formulario['password']):
            js_message = 'Password must have at least 6 characters, 1 number &    1 capital letter'
            return js_message
        
        if formulario['password'] != formulario['confirm_password']:
            js_message = "Passwords don't match"
            return js_message

        js_message = 'correct info'

        return js_message

    @staticmethod
    def validate_user_update(formulario):
        if (len(formulario['name'])) <3:
            js_message = 'Name must be at least 3 letters long'
            return js_message

        if len(formulario['nickname']) <3:
            js_message = 'Nickname must be at least 3 letters long'
            return js_message

        if not EMAIL_REGEX.match(formulario['email']):
            js_message = 'Invalid email'
            return js_message

        if not PASSWORD_REGEX.match(formulario['password']):
            js_message = 'Password must have at least 6 characters, 1 number &    1 capital letter'
            return js_message
        
        if formulario['password'] != formulario['confirm_password']:
            js_message = "Passwords don't match"
            return js_message

        js_message = 'correct info'
        return js_message

    @classmethod
    def update_user(cls, formulario):
        query = "UPDATE users SET name = %(name)s, nickname = %(nickname)s, email = %(email)s, password = %(password)s WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        return result

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        if len(result) <1:
            return False
        else:
            user= cls(result[0])
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        user = cls(result[0])
        return user

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('topmovies').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('topmovies').query_db(query)
        users = []
        for result in results:
            users.append(cls(result))
        return users

