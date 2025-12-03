from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)


original_books_df = pd.read_csv("data/Books.csv")


model_data = pickle.load(open("data/recommender.pkl", "rb"))
model_knn = model_data["model_knn"]
book_features_df = model_data["book_features_df"]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_similar", methods=["POST"])
def get_similar():
    data = request.get_json()
    book_name = data.get("book_name")

    if not book_name:
        return jsonify({"error": "No book name given"}), 400

    recommendations = recommend(book_name)
    return jsonify({"recommendations": recommendations})

def recommend(book_title):

  
    if book_title not in book_features_df.index:
        return []

    query_index = book_features_df.index.get_loc(book_title)

    distances, indices = model_knn.kneighbors(
        book_features_df.iloc[query_index, :].values.reshape(1, -1),
        n_neighbors=6
    )

    results = []
    for i in range(1, 6):      
        idx = indices.flatten()[i]
        title = book_features_df.index[idx]

        author_row = original_books_df.loc[
            original_books_df["Book-Title"] == title, "Book-Author"
        ]

        author = author_row.values[0] if len(author_row) else "Unknown Author"

        results.append({
            "Book-Title": title,
            "Book-Author": author
        })

    return results

if __name__ == "__main__":
    app.run(debug=True)
