def get_similar_movies(movie_title, similarity_df, n=5):
    if movie_title not in similarity_df.columns:
        return []
    similar_scores = similarity_df[movie_title].sort_values(ascending=False)
    return list(similar_scores.iloc[1:n+1].index)
