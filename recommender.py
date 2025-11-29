import pandas as pd

books = pd.read_csv("data/Books.csv")
ratings = pd.read_csv("data/Ratings.csv")
users = pd.read_csv("data/Users.csv")

book_data = books.dropna(axis=0)
book_features = ['ISBN','Book-Title','Book-Author']
book = book_data[book_features]
book.drop_duplicates(subset="ISBN", inplace=True)
#book

#ratings
ratings = ratings[ratings['Book-Rating'] > 0]
print(ratings)

#merge book with ratings
df = ratings.merge(book, on="ISBN")
print(df.head())


print(book.shape)
print(ratings.shape)
print(users.shape)
