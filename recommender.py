import pandas as pd

books = pd.read_csv("data/Books.csv")
#ratings = pd.read_csv("data/Ratings.csv")
#users = pd.read_csv("data/Users.csv")

#book
book_data = books.dropna(axis=0)
book_features = ['ISBN','Book-Title','Book-Author','Publisher']
book = book_data[book_features]
book.drop_duplicates(subset="ISBN", inplace=True)

#ratings
#ratings = ratings[ratings['Book-Rating'] > 0]
#ratings_features = ['ISBN','Book-Rating']
#ratings = ratings[ratings_features]


#merge book with ratings
#df = ratings.merge(book, on="ISBN")
#print(df.head())




print(book.shape)
#print(ratings.shape)
#print(users.shape)
