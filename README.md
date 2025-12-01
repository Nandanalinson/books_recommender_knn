# 📚 Book Recommendation System

A simple Flask-based web application that recommends similar books based on author, publisher, and title-word similarity. Users can enter a book name and instantly get the top 5 recommended books.

---

## 🚀 Features

* 🔍 **Search for any book**
* 🤝 **Similarity-based recommendations** (author, publisher, and title-word match)
* ⚡ Fast — no ML model required
* 🎨 Clean minimal UI (HTML + CSS + JS)
* 🌐 Built with Flask (Python)
* 🗂️ Uses a preprocessed `books.pkl` dataset

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Data:** Pandas (Pickle dataset)
* **Server Communication:** Fetch API (JSON)

---

## 📁 Project Structure

```
project/
│
├── app.py
├── recommender.py
├── data/
│   └── books.pkl
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── script.js
└── README.md
```

---

## 💡 How Recommendations Work

When the user types a book name:

1. We search for the closest matching book title in the dataset.
2. Take that book as the *target book*.
3. For every other book, we calculate a **similarity score**:

   * +3 points → Same **author**
   * +1 point → Same **publisher**
   * +1 point for each common **word in the title**
4. Filter out books with zero score.
5. Sort by score in descending order:

   ```python
   recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)
   ```
6. Return **top 5 recommendations**.

This ensures the user always sees the most relevant books first.

---

## 🧪 Example Response

### User input:

```
"Harry Potter"
```

### Output JSON:

```json
{
  "recommendations": [
    {
      "title": "Harry Potter and the Chamber of Secrets",
      "author": "J.K. Rowling",
      "publisher": "Scholastic",
      "score": 7
    },
    ...
  ]
}
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
```

### 2️⃣ Install dependencies

```
pip install flask pandas
```

### 3️⃣ Add the dataset

Place your `books.pkl` file inside the **data/** directory.

### 4️⃣ Run the Flask app

```
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🖥️ API Endpoint

### **POST /get_similar**

**Request Body**

```json
{
  "book_name": "Harry Potter"
}
```

**Response**

```json
{
  "recommendations": [
    {
      "title": "Harry Potter and the Goblet of Fire",
      "author": "J.K. Rowling",
      "publisher": "Scholastic",
      "score": 6
    }
  ]
}
```

---

## 🧩 Frontend Explanation

### `index.html`

* Contains input box and button.
* Displays results.

### `script.js`

Sends user input to Flask:

```javascript
fetch("/get_similar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ book_name })
})
```

Shows "Searching..." while waiting:

```javascript
results.innerHTML = "<li>Searching...</li>";
```

### `styles.css`

* Minimal styling
* Centered layout

---

## 🧠 Why This Works (Simple ML Concept)

Although not using a machine-learning model, the system behaves like a **rule-based recommender**:

* It uses *content-based filtering*
* Compares attributes of one book with others
* Scores similarity
* Ranks and returns the top results

This is a beginner-friendly way to implement a recommender system without training a model.

---

## 📌 Future Improvements

You can upgrade this app later by adding:

* TF-IDF text vectorization
* Cosine similarity
* A trained recommendation model
* User ratings + collaborative filtering
* Pagination and UI improvements

---

## 📄 License

This project is open-source under the MIT License.

