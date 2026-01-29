import streamlit as st
from recommend import recommend
import pandas as pd

movies = pd.read_csv("tmdb_5000_movies.csv")
movie_list = movies['title'].values

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
        