# 📚 Book Recommendation System (KNN + Flask)

This project is a **Book Recommendation System** that uses **Collaborative Filtering** with **K-Nearest Neighbors (KNN)** to recommend similar books to users based on rating patterns.
The machine learning model is trained in a Jupyter Notebook, saved as a **PKL file**, and integrated into a **Flask web application** for real-time recommendations.

---

## 🚀 Project Features

### **🔹 Machine Learning**

* Uses **User–Book rating matrix** generated from:

  * `Books.csv`
  * `Ratings.csv`
* Converts matrix into sparse format.
* Trains a **KNN model (cosine similarity)** for finding nearest books.
* Saves the model & data as `recommender.pkl`.

### **🔹 Backend (Flask)**

* Loads the PKL model.
* Accepts user input (book name) via API.
* Returns top 5 similar books with similarity distance.

### **🔹 Frontend**

* HTML + CSS + JavaScript.
* Search bar for book name.
* Dynamically displays recommendations.

---

## 📂 Project Structure

```
project/
│── data/
│    ├── Books.csv
│    ├── Ratings.csv
│    ├── recommender.pkl
│
│── main.py
│── templates/
│    ├── index.html
│
│── static/
│    ├── css/styles.css
│    ├── js/script.js
│
│── notebook/
│    ├── model_build.ipynb
│
│── README.md
```

---

## 🧠 ML Pipeline Explained

### **1️⃣ Load and Clean Data**

```python
df_book['Year-Of-Publication'] = pd.to_numeric(df_book['Year-Of-Publication'], errors='coerce')
df_book = df_book.dropna(subset=['Year-Of-Publication'])
df_book = df_book[df_book['Year-Of-Publication'] > 1900]
```

✔ Ensures valid years
✔ Removes corrupted rows
✔ Keeps only meaningful book data

---

### **2️⃣ Merge Books and Ratings**

```python
merged_df = pd.merge(df_book, ratings, on='ISBN')
```

Creates a single dataframe with all relevant information.

---

### **3️⃣ Filter Popular Books (minimum 50 ratings)**

```python
popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
```

✔ Reduces noise
✔ Ensures better recommendations

---

### **4️⃣ Create User–Book Matrix**

```python
book_features_df = rating_popular_book.pivot_table(
    index='Book-Title',
    columns='User-ID',
    values='Book-Rating'
).fillna(0)
```

Matrix shape example:

| Book   | User1 | User2 | User3 |
| ------ | ----- | ----- | ----- |
| Book A | 5     | 0     | 7     |
| Book B | 0     | 8     | 6     |

---

### **5️⃣ Convert to Sparse Matrix**

```python
book_features_df_matrix = csr_matrix(book_features_df.values)
```

Speeds up KNN calculations.

---

### **6️⃣ Train KNN**

```python
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(book_features_df_matrix)
```

---

### **7️⃣ Save Model**

```python
pickle.dump(model_data, open("data/recommender.pkl", "wb"))
```

---

### **8️⃣ Use in Flask**

Flask loads the PKL file:

```python
model_data = pickle.load(open("data/recommender.pkl", "rb"))
model_knn = model_data["model_knn"]
book_features_df = model_data["book_features_df"]
```

Recommendation function:

```python
distances, indices = model_knn.kneighbors(
    book_features_df.iloc[query_index,:].values.reshape(1, -1),
    n_neighbors=6
)
```

---

## 🧪 Model Evaluation

You computed:

```
precision@k = 0.00107
recall@k    = 0.000099
f1@k        = 0.000181
```

Why low?

* Collaborative filtering with **implicit ratings** is noisy
* No user personalization
* Book ratings dataset is sparse

You can improve with:

* Matrix factorization (SVD)
* Hybrid filtering (content + CF)
* Removing cold start users
* Normalizing ratings

---

## 📊 Visual Evaluation Graph

A simple evaluation graph is included (precision/recall/F1).

---

## ▶️ How to Run This Project

### **1. Install dependencies**

```
pip install flask pandas numpy scikit-learn scipy
```

### **2. Train model**

Run `model_build.ipynb` to create `recommender.pkl`.

### **3. Start Flask**

```
python main.py
```

Visit:
👉 `http://127.0.0.1:5000/`

---

## 📝 API Endpoint

### **POST /get_similar**

**Request:**

```json
{
  "book_name": "Harry Potter and the Philosopher's Stone"
}
```

**Response:**

```json
{
  "recommendations": [
    { "title": "Another Book", "distance": 0.12 },
    { "title": "Some Book", "distance": 0.15 }
  ]
}
```

---

## ⭐ Future Improvements

* Add covers & descriptions using Google Books API
* Add user login & personalization
* Implement Matrix Factorization (SVD, ALS)
* Deploy on Render/DigitalOcean/AWS
