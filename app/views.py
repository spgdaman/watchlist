from flask import render_template
from app import app
from .requests import get_movie, show_movie

# Views
@app.route('/')
def index():
    popular_movies = get_movie('popular')
    upcoming_movies = get_movie('upcoming')
    now_showing_movies = get_movie('now_playing')
    title = "Home - Welcome to the best movie review website"
    return render_template('index.html',title=title, popular=popular_movies, upcoming=upcoming_movies, now=now_showing_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = show_movie(movie_id)
    title = f'{movie.original_title}'
    return render_template('movie.html', title=title, movie=movie)