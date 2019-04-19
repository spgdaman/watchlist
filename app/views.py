from flask import render_template, request,redirect,url_for
from app import app
from .requests import get_movie, show_movie, search_movie
from .models import reviews
from .forms import ReviewForm
Review = reviews.Review


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
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html', title=title, movie=movie, reviews=reviews)

@app.route('/search/<string:movie_name>')
def search(movie_name):
    right_name = movie_name.split(" ")
    movie_name_format = "+".join(right_name)
    searched = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', search = searched, title=title)

@app.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = show_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',movie_id=movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)