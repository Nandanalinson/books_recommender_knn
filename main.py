from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model
model_data = pickle.load(open("data/recommender.pkl", "rb"))
pt = model_data["pt"]
similarity_scores = model_data["similarity_scores"]
books = model_data["book"]


#https://www.kaggle.com/code/swas06/bookrecommendation-colloborativefiltering#Colloborative-Filtering--Based-Recommendation-System


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_similar", methods=["POST"])
def get_similar():
    data = request.get_json()
    book_name = data.get("book_name")
    recommendations = recommend(book_name)
    return jsonify({"recommendations": recommendations})

def recommend(book_title):
 
    if book_title not in pt.index:
        raise Exception("Book not found")

   
    index = np.where(pt.index == book_title)[0][0]

   
    similar_items = sorted(list(enumerate(similarity_scores[index])), 
                           reverse=True, key=lambda x: x[1])[1:6]

    results = []
    for i in similar_items:
        book = pt.index[i[0]]
        author = books[books['Book-Title'] == book]['Book-Author'].values[0]
        results.append({
            "Book-Title": book,
            "Book-Author": author
        })

    return results

if __name__ == "__main__":
    app.run(debug=True)
