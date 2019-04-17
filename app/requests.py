from app import app
import requests

# Getting api key
api_key = app.config['MOVIE_API_KEY']

def get_movie(category):
    api_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(category,api_key)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data["results"]

def show_movie(id):
    api_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(id,api_key)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data