# 🎬 Movie Recommender System

A Machine Learning based Movie Recommender System that recommends movies similar to the movie selected by the user.

The system uses **Content-Based Filtering** and **Cosine Similarity** to find movies with similar content and generate personalized recommendations.

## 🚀 Features

- 🎥 Select a movie from the available movie list
- 🤖 Get Top 5 similar movie recommendations
- 📊 Uses Content-Based Recommendation
- 🔍 Calculates similarity using Cosine Similarity
- ⚡ Simple and interactive Streamlit interface
- 🎯 Displays the similarity match percentage for recommended movies

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## 🧠 How It Works

1. The movie dataset is loaded and preprocessed.
2. Important movie features are combined to represent each movie.
3. Movie features are converted into numerical vectors.
4. Cosine Similarity is calculated between movies.
5. When a user selects a movie, the system finds the most similar movies.
6. The Top 5 recommendations are displayed with their content similarity percentage.

## 📂 Project Structure

```text
Movie-Recommender/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
