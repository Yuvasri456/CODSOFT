import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies_data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genres': ['Action|Adventure|Sci-Fi', 'Adventure|Drama|Fantasy', 'Comedy|Romance', 'Action|Adventure|Fantasy', 'Drama|Thriller']
}

movies_df = pd.DataFrame(movies_data)
user_favorite_movie = 'Movie A'
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Get the index of the user's favorite movie
movie_index = movies_df[movies_df['Title'] == user_favorite_movie].index[0]

# Get the pairwise similarity scores with the user's favorite movie
similar_movies = list(enumerate(cosine_sim[movie_index]))
similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
top_similar_movies = similar_movies[1:6]
print(f"Top 5 Recommendations for {user_favorite_movie}:")
for idx in range(len(top_similar_movies)):
    movie_idx, score = top_similar_movies[idx]
    print(f"Movie: {movies_df['Title'].iloc[movie_idx]}, Similarity Score: {score}")
