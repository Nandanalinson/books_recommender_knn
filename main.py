from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd
from recommender import recommend_knn

app = Flask(__name__)

df = pd.read_pickle("data/books_df.pkl")
vectorizer = pickle.load(open("data/vectorizer.pkl", "rb"))
model = pickle.load(open("data/knn.pkl", "rb"))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_similar", methods=["POST"])
def get_similar():
    data = request.get_json(silent=True)
    book_name = data.get("book_name")  # <-- FIX

    recommendations = recommend_knn(
        book_name,
        df,
        vectorizer,
        model
    )

    return jsonify({"recommendations": recommendations})  # <-- FIX

if __name__ == "__main__":
    app.run(debug=True)
