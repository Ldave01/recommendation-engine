import pandas as pd

def load_and_merge_data(ratings_path, movies_path):
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)
    data = pd.merge(ratings, movies, on='movieId')
    return data
