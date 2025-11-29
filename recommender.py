import pandas as pd

books = pd.read_csv("data/Books.csv")
ratings = pd.read_csv("data/Ratings.csv")
users = pd.read_csv("data/Users.csv")

book_data = books.dropna(axis=0)
book_features = ['ISBN','Book-Title','Book-Author']
b = book_data[book_features]
print(b)

ratings_data = ratings[ratings['Book-Rating'] > 0]

print(ratings_data)

print(books.shape)
print(book_data.shape)
print(ratings.shape)
print(ratings_data.shape)
print(users.shape)
