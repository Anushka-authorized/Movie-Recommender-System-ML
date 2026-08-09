import requests
import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse = True, key = lambda x:x[1])

    recommended_movies = []
  
    for i in distances[1:6]:
        movie_id = i[0]
    

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    name = recommend(selected_movie_name)

    for i in name:
        st.write(i)
