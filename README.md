# 🎬 Movie Recommendation Engine

This project is an interactive movie recommendation system built using **collaborative filtering** and deployed with **Streamlit Cloud**. It uses the MovieLens dataset to recommend movies similar to a selected title based on user ratings.

## 📌 Features

- User-based and item-based collaborative filtering
- Cosine similarity for movie similarity scoring
- Clean and interactive Streamlit UI
- Based on MovieLens educational dataset
- Deployable to Streamlit Cloud for live demos

## 🧰 Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Streamlit

## 📁 Project Structure

recommendation-engine/
├── app.py
├── data/
│ ├── movies.csv
│ └── ratings.csv
├── src/
│ ├── data_preprocessing.py
│ ├── similarity_calculator.py
│ └── recommender.py
├── requirements.txt
└── README.md


## ▶️ How to Run Locally

1. Clone the repo  
   `git clone https://github.com/Ldave01/recommendation-engine.git`

2. Navigate into the project  
   `cd recommendation-engine`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Run the app  
   `streamlit run app.py`

## 🚀 Live Demo

Try it here: [recommendation-engine.streamlit.app](https://recommendation-engine.streamlit.app)

## 📂 Dataset

- MovieLens dataset for education & development: [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)

## 📜 License

This project is licensed under the MIT License.
