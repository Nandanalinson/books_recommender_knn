from flask import Flask, render_template, request, jsonify
from recommender import get_similar_books

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_similar", methods=["POST"])
def get_similar():
    data = request.get_json()

    book_name = data.get("book_name")

    if not book_name:
        return jsonify({"error": "No book name provided"}), 400

    recommendations = get_similar_books(book_name)
    

    return jsonify({"recommendations": recommendations})


if __name__ == "__main__":
    app.run(debug=True)
