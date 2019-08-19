from flask import render_template,request,redirect,url_for,abort
from app import mail
from . import main
from ..request import get_movies, get_movie
from ..models import *
from flask_login import login_required
from flask_mail import Mail, Message
from .forms import *
from .. import db
import http.client
import requests, json
from ..models import *


@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and movie list
    '''

    # Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie,
                           now_showing=now_showing_movie)


@main.route('/movie/<int:id>')
@login_required
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html',title = title,movie = movie)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    mygenres= Genres.query.all()

    url=("http://api.themoviedb.org/3/genre/movie/list?language=en-US&api_key=63fcd85379cd2a0aaeed015f96dcddf2")
    response=requests.get(url).json()
    x = list(response['genres'])
    genres=[]
    for i in x:
        genre=(i['name'])
        genres.append(genre)
    print(genres)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, genres= genres, mygenres=mygenres)


@main.route('/user/<uname>/genre/new/', methods = ['GET','POST'])
def new_genre(uname):
    form = GenreForm()
    user = User.query.filter_by(username = uname).first()

    if form.validate_on_submit():
        genre = form.name.data
        new_genre = Genres(genre)
        db.session.add(new_genre)
        db.session.commit()
        if user.is_authenticated:
            return redirect(url_for('main.profile',uname=uname))

    title = 'Add a genre'
    return render_template('new_genre.html',title = title, genre_form=form, user = user)



