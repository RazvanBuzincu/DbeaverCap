import requests
import requests_cache
import json


requests_cache.install_cache('omdb_cache', backend='sqlite')

def get_movie_details(title):
    url = "http://www.omdbapi.com/"

    
    params = {
        "t": title,  
        "apikey": "8882013b"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'Error' not in data:
        
        movie_details = {
            'title': data.get('Title', ''),
            'year': data.get('Year', ''),
            'director': data.get('Director', ''),
            'poster': data.get('Poster', ''),  
            'plot': data.get('Plot', '')
        }
        return movie_details
    else:
        return "Movie not found."

def get_image(title):
    movie_details = get_movie_details(title)
    if movie_details != "Movie not found.":
        return movie_details.get('poster', 'URL_to_default_poster_if_needed')
    else:
        return 'URL_to_default_poster_if_needed'  
