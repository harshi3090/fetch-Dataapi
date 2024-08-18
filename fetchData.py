import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("BEARER_TOKEN")
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data/getPopularMovies.json", "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_top_rated_movies():
    url = "https://api.themoviedb.org/3/movie/top_rated"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("BEARER_TOKEN")
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data/getTopRatedMovies.json", "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_movie_recommendations():
    url = "https://api.themoviedb.org/3/movie/573435/recommendations"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("BEARER_TOKEN")
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data/getMovieRecommendations.json", "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

get_popular_movies()
get_top_rated_movies()
get_movie_recommendations()
