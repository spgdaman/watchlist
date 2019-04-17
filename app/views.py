from flask import render_template
from app import app
from . import get_movies

# Views
@app.route('/')
def index():
    popular_movies = get_movies('popular')
    title = "Home - Welcome to the best movie review website"
    return render_template('index.html',title=title, popular=popular_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html', id=movie_id)