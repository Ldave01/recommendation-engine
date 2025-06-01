import streamlit as st
from src.data_preprocessing import load_and_merge_data
from src.similarity_calculator import create_user_item_matrix, compute_similarity_matrix
from src.recommender import get_similar_movies

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation Engine")
st.markdown("Select a movie and get similar movie suggestions!")

# Load & prepare data
data = load_and_merge_data("data/ratings.csv", "data/movies.csv")
user_item_matrix = create_user_item_matrix(data)
similarity_df = compute_similarity_matrix(user_item_matrix)

movie_list = sorted(user_item_matrix.columns.dropna())

selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recommendations = get_similar_movies(selected_movie, similarity_df)
    if recommendations:
        st.success("Here are some similar movies:")
        for idx, rec in enumerate(recommendations, start=1):
            st.write(f"{idx}. {rec}")
    else:
        st.warning("Sorry, no recommendations found.")
