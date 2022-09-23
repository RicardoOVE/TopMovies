from flask import render_template, redirect, session, request, flash
from flask_app import app

#importación del modelo
from flask_app.models.users import User
from flask_app.models.movies import Movie
from flask_app.models.interactions import Interaction

@app.route('/movies')
def movies():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario)

    #movies = Movies.get_all()

    return render_template('movies.html', user=user) #, movies=movies

@app.route('/movie/<int:movie_id>')
def show_movie(movie_id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    formulario_movie = { "id": movie_id }

    user = User.get_by_id(formulario)
    movie = Movie.get_by_id(formulario_movie)
    #poster_path = "{{url_for('static',filename='images/posters/1.jpg')}}"
    
    return render_template('show_movie.html', user=user, movie = movie, movie_id = str(movie_id))

@app.route('/movie/<int:movie_id>/like')
def like_movie(movie_id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    formulario_movie = { "id": movie_id
    }

    formulario_interaction ={
        "user_id": session['user_id'],
        "movie_id": movie_id
    }

    user = User.get_by_id(formulario)
    movie = Movie.get_by_id(formulario_movie)
    result = Interaction.already_liked(formulario_interaction)
    
    if result == 0 or result == 'bool':
        formulario_interaction = { 
        "comment": "",
        "liked": "1",
        "disliked": "0",
        "favorited": "0",
        "user_id": session['user_id'],
        "movie_id": movie_id,
        }
        movie.save_interaction(formulario_interaction)
        movie = Movie.like(formulario_movie)
    
    return render_template('show_movie.html', user=user, movie = movie, movie_id = str(movie_id))

@app.route('/movie/<int:movie_id>/dislike')
def dislike_movie(movie_id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    formulario_movie = { "id": movie_id
    }

    formulario_interaction ={
        "user_id": session['user_id'],
        "movie_id": movie_id
    }

    user = User.get_by_id(formulario)
    movie = Movie.get_by_id(formulario_movie)
    result = Interaction.already_liked(formulario_interaction)
    
    if result == 0 or result == 'bool':
        formulario_interaction = { 
        "comment": "",
        "liked": "0",
        "disliked": "1",
        "favorited": "0",
        "user_id": session['user_id'],
        "movie_id": movie_id,
        }
        movie.save_interaction(formulario_interaction)
        movie = Movie.dislike(formulario_movie)
    
    return render_template('show_movie.html', user=user, movie = movie, movie_id = str(movie_id))

@app.route('/movie/<int:movie_id>/favorite')
def favorite_movie(movie_id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    formulario_movie = { "id": movie_id
    }

    formulario_interaction ={
        "user_id": session['user_id'],
        "movie_id": movie_id
    }

    user = User.get_by_id(formulario)
    movie = Movie.get_by_id(formulario_movie)
    result = Interaction.already_favorited(formulario_interaction)
    
    if result == 0 or result == 'bool':
        formulario_interaction = { 
        "comment": "",
        "liked": "0",
        "disliked": "0",
        "favorited": "1",
        "user_id": session['user_id'],
        "movie_id": movie_id,
        }
        movie.save_interaction(formulario_interaction)
        movie = Movie.favorite(formulario_movie)
    
    return render_template('show_movie.html', user=user, movie = movie, movie_id = str(movie_id))