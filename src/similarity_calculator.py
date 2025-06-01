import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def create_user_item_matrix(data):
    return data.pivot_table(index='userId', columns='title', values='rating')

def compute_similarity_matrix(user_item_matrix):
    filled = user_item_matrix.fillna(0)
    similarity = cosine_similarity(filled.T)
    similarity_df = pd.DataFrame(similarity,
                                 index=user_item_matrix.columns,
                                 columns=user_item_matrix.columns)
    return similarity_df
