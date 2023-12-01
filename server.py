from typing import Union
from fastapi import FastAPI
import pickle
import requests
import os

# use .env file to load the environment variables
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# Loading the API_KEY
API_KEY=os.getenv("API_KEY")

movies = pickle.load(open('./helpers/movie_list.pkl', 'rb'))
similarity = pickle.load(open('./helpers/similarity_movies.pkl', 'rb'))

app = FastAPI()

# remove cors error
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

@app.get("/")
def read_root():
    return movies['title'].values.tolist()

@app.get("/recommend/{movie}")
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_data = {}
    for i in distances[1:10]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        movie_poster = fetch_poster(movie_id)
        movie_name = movies.iloc[i[0]].title
        recommended_movie_data[movie_name] = movie_poster
    return [recommended_movie_data]
    