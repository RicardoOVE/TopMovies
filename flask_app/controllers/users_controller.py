#from crypt import methods
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app

from flask_app.models.users import User
from flask_app.models.movies import Movie

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_page')
def login_page():
    if 'user_id' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/sign_in_page')
def sign_in_page():
    if 'user_id' in session:
        return redirect('/')
    return render_template('sign_in.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def login():

    user = User.get_by_email(request.form)

    if not user:
        return jsonify(message='email not found')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return jsonify(message='wrong password')
    
    session['user_id'] = user.id

    return jsonify(message='correct')

@app.route('/sign_in', methods=['POST'])
def sign_in():
    
    js_message= User.validate_user(request.form)

    if js_message == 'correct info':
        pwd = bcrypt.generate_password_hash(request.form['password'])

        formulario = {
            "name": request.form['name'], 
            "nickname": request.form['nickname'],
            "email": request.form['email'],
            "password": pwd
        }

        id = User.save(formulario)
        session['user_id'] = id
        js_message = 'correct'

    return jsonify(message=js_message)

@app.route('/profile/')
def def_profile():
    if 'user_id' not in session:
        return redirect('/')
    return redirect('/profile/<int:id>')

@app.route('/profile/<int:id>')
def profile(id):
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario)

    movies_ids = Movie.get_all_liked(formulario)
    disliked_ids = Movie.get_all_disliked(formulario)
    favorited_ids = Movie.get_all_favorited(formulario)

    return render_template('my_profile.html', user=user, movies_ids = movies_ids, disliked_ids = disliked_ids, favorited_ids = favorited_ids)

@app.route('/update/user', methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/')
    
    #olduser = User.get_by_email(request.form)
    
    js_message= User.validate_user_update(request.form) #, olduser.nickname, olduser.email

    if js_message == 'correct info':
        pwd = bcrypt.generate_password_hash(request.form['password'])

        formulario = {
                "name": request.form['name'], 
                "nickname": request.form['nickname'],
                "email": request.form['email'],
                "password": pwd,
                "id": session['user_id']
            }
    
        User.update_user(formulario)
        
        js_message = 'correct'

    return jsonify(message=js_message)

@app.route('/delete/user/<int:id>')
def delete_user(id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    User.delete(formulario)

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear() #Elimine la sesión
    return redirect('/')