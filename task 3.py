import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import pairwise_distances
data = {
    'User': ['User1', 'User1', 'User1', 'User2', 'User2', 'User3', 'User3', 'User3'],
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie1', 'Movie2', 'Movie2', 'Movie3', 'Movie4'],
    'Rating': [5, 4, 3, 4, 5, 4, 3, 5]
}

df = pd.DataFrame(data)
user_item_matrix = df.pivot(index='User', columns='Movie', values='Rating').fillna(0)
user_similarity = 1 - pairwise_distances(user_item_matrix.values, metric='cosine')
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
def get_movie_recommendations(user):
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]
    user_movies = user_item_matrix.loc[user]
    recommended_movies = []

    for other_user in similar_users:
        other_user_movies = user_item_matrix.loc[other_user]
        new_movies = other_user_movies[other_user_movies > 0].index.difference(user_movies[user_movies == 0].index)
        recommended_movies.extend(new_movies)

    return set(recommended_movies)
user_to_recommend = 'User1'
recommendations = get_movie_recommendations(user_to_recommend)

print(f"Recommended movies for {user_to_recommend}: {', '.join(recommendations)}")
