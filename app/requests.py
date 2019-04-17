from app import app
import requests

# Getting api key
api_key = app.config['MOVIE_API_KEY']

def get_movie():