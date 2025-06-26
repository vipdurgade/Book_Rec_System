# 📚 Book Recommendation System

This project is a **machine learning-based book recommendation system** that suggests personalized books to users based on their reading preferences. Built using collaborative filtering techniques, it leverages user-item interaction data to predict books that a user is likely to enjoy.

## 🔍 Project Overview

The Book Recommendation System is designed to provide efficient and accurate book suggestions using a user-based collaborative filtering algorithm. It analyzes patterns in user ratings to generate personalized recommendations.

**Notebook:**  
🔗 [Book Recommendation System.ipynb](https://github.com/vipdurgade/Book_Rec_System/blob/main/Book%20Recommendation%20%20System%20.ipynb)

## 💡 Features

- 📊 Exploratory Data Analysis (EDA) for understanding rating patterns and user engagement
- 🧠 Similarity-based recommendation engine using **cosine similarity**
- 🔍 Top-N recommendations for any user
- ✅ Scalable and easily extendable for other recommendation strategies (e.g., content-based, hybrid)

## 🛠️ Technologies Used

- **Python**
- **Pandas & NumPy** – Data manipulation and analysis
- **Scikit-learn** – Similarity computation
- **Matplotlib & Seaborn** – Data visualization
- **Jupyter Notebook**

## 📁 Dataset

- The dataset includes user ratings for different books.
- Columns used: `user_id`, `book_title`, `book_rating`
- The data is filtered to include only books with more than 200 ratings to improve quality.

## ⚙️ How it Works

1. **Data Preprocessing:** Clean and merge datasets, filter out sparse data.
2. **Pivot Table Creation:** Build a user-item matrix of book ratings.
3. **Similarity Calculation:** Use cosine similarity to find similar users or books.
4. **Recommendation Function:** Generate personalized recommendations.

## 🧪 Example Output

```python
recommend_books("The Hobbit", top_n=5)
