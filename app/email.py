from flask_mail import Message, Mail
from flask import render_template
from . import mail
import requests, random
from .models import *
from flask import render_template,request,redirect,url_for,abort


def mail_message(subject,template,to,**kwargs):
    sender_email = 'munenecyp@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)


def recommendation(subject, template, to, **kwargs):

    # # get now_playing recommendations by their genre_ids
    # url = "https://api.themoviedb.org/3/movie/now_playing?&api_key=63fcd85379cd2a0aaeed015f96dcddf2"
    # response = requests.get(url).json()
    # x = list(response['results'])
    # genres_ids = []
    # for i in x:
    #     genres = (i['genre_ids'])
    #     genres_ids.append(genres)
    #
    # # get a list of all genres ids
    # url = ("http://api.themoviedb.org/3/genre/movie/list?language=en-US&api_key=63fcd85379cd2a0aaeed015f96dcddf2")
    # response = requests.get(url).json()
    # x = list(response['genres'])
    # all_genres = []
    # for i in x:
    #     genre = (i['id'])
    #     all_genres.append(genre)
    #
    # # list of genre ids that appear in both lists
    # duplicates_list=[]
    # for i in all_genres:
    #     for x in genres_ids
    #         if x  in genres_ids

    # convert genre_ids list into genre_names list

    sender_email = 'munenecyp@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)

    # get now_playing recommendations
    url = "https://api.themoviedb.org/3/movie/now_playing?&api_key=63fcd85379cd2a0aaeed015f96dcddf2"
    response = requests.get(url).json()
    recommendations = list(response['results'])
    random_movie = random.choice(recommendations)
    return render_template('templates/email/recommendation.html', random=random_movie)