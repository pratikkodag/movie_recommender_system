import streamlit as st 
import pickle
import numpy
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity
# Custom CSS to style the columns, background, and title
st.markdown("""
    <style>
    /* Netflix-style dark gradient background */
    .main {
        background: linear-gradient(to bottom, #141414, #2c2c2c); /* Dark gradient */
        padding: 20px;
        color: white; /* White text color */
    }

    /* Title styling similar to Netflix */
    .title h1 {
        color: #E50914; /* Netflix red color */
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8); /* Strong shadow for contrast */
        font-size: 3.5em;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Helvetica', sans-serif;
    }

    /* Column content styling */
    .column-content {
        text-align: center;
        background-color: rgba(30, 30, 30, 0.9); /* Dark semi-transparent background */
        border: 1px solid #444444;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
        color: white; /* White text inside columns */
    }

    .column-content:hover {
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.6); /* Stronger shadow on hover */
    }

    /* Button styling */
    .stButton button {
        background-color: #E50914; /* Netflix red button */
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #b50710; /* Darker red on hover */
    }
    </style>
    """, unsafe_allow_html=True)


def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?language=en-US&api_key=7afc721b9f668ed527467e70e8fd63ec'.format(movie_id),timeout=30)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0] ## to get the index of the movies
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True ,key=lambda x:x[1])[1:8]
    recommended_movies=[]
    recommended_movies_posters = []

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters
    
movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity =pickle.load(open('similarity.pkl','rb'))


st.markdown('<div class="title"><h1>🎬 Movie Recommender System</h1></div>', unsafe_allow_html=True)
selected_movie_name=st.selectbox("Discover your next favorite movie!",movies['title'].values)

if  st.button("Recommend"):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4= st.columns(4)
    with col1 :
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    col5 ,col6,col7=st.columns(3)
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    
