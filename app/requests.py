from app import app
from .models import movie
import requests
import urllib.request, json

Movie = movie.Movie

# Getting api key
api_key = app.config['MOVIE_API_KEY']

def get_movie(category):
    api_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(category,api_key)

    response = requests.get(api_url)

    data = response.json()
    dict_list = data["results"]    
    
    results = process_results(dict_list)    

    return results

    # with urllib.request.urlopen(api_url) as url:
    #     get_movies_data = url.read()
    #     get_movies_response = json.loads(get_movies_data)

    #     movie_results = None

    #     if get_movies_response['results']:
    #         movie_results_list = get_movies_response['results']
    #         movie_results = process_results(movie_results_list)

    # return movie_results

def show_movie(id):
    api_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(id,api_key)

    response = requests.get(api_url)
   
    data = response.json()

    if data:
        id = data.get('id')
        title = data.get('original_title')
        overview = data.get('overview')
        poster = data.get('poster_path')
        vote_average = data.get('vote_average')
        vote_count = data.get('vote_count')

    results = Movie(id,title,overview,poster,vote_average,vote_count)
    return results
    


def search_movie(movie_name):
#     api_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)

#     response = requests.get(api_url)

#     data = response.json()
#     dict_list = data["results"]    
    
#     results = process_results(dict_list)    

#     return results
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item['id']
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
        movie_results.append(movie_object)

    return movie_results