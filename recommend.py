import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("tmdb_5000_movies.csv")
movies['overview'] = movies['overview'].fillna('')

# Convert text to feature vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['overview']).toarray()

# Compute similarity matrix
similarity = cosine_similarity(vectors)

def recommend(movie):
    # Find index of the movie
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Sort movies by similarity
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies