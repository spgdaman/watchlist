from flask import render_template, request,redirect,url_for
from app import app
from .requests import get_movie, show_movie, search_movie

# Views
@app.route('/')
def index():
    popular_movies = get_movie('popular')
    upcoming_movies = get_movie('upcoming')
    now_showing_movies = get_movie('now_playing')
    title = "Home - Welcome to the best movie review website"

    search = request.args.get("movie_query")

    if search:
        return redirect(url_for('search',movie_name = search))
    else:
        return render_template('index.html',title=title, popular=popular_movies, upcoming=upcoming_movies, now=now_showing_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = show_movie(movie_id)
    title = f'{movie.title}'
    return render_template('movie.html', title=title, movie=movie)

@app.route('/search/<string:movie_name>')
def search(movie_name):
    right_name = movie_name.split(" ")
    movie_name_format = "+".join(right_name)
    searched = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', search = searched, title=title)
