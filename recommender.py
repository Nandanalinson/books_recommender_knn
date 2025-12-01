import pandas as pd

books_df = pd.read_pickle("data/books.pkl")

# Common useless words to ignore
STOPWORDS = {"the", "a", "an", "and", "to", "of", "in", "for", "guide", 
             "world", "companion", "reader", "handbook", "book", "life"}

def clean_words(title):
    words = set(title.lower().split())
    return words - STOPWORDS


def get_similar_books(book_name):
    book_name = book_name.strip().lower()

    # Find best match
    matches = books_df[books_df["Book-Title"].str.lower().str.contains(book_name)]

    if matches.empty:
        return []

    target = matches.iloc[0]
    target_author = target["Book-Author"]
    target_publisher = target["Publisher"]
    target_words = clean_words(target["Book-Title"])

    recommendations = []

    for _, row in books_df.iterrows():
        score = 0

        
        if row["Book-Author"] == target_author:
            score += 5

        if row["Publisher"] == target_publisher:
            score += 1
        row_words = clean_words(row["Book-Title"])


        score += len(target_words.intersection(row_words))

        if score > 0 and row["Book-Title"] != target["Book-Title"]:
            recommendations.append({
                "title": row["Book-Title"],
                "author": row["Book-Author"],
                "publisher": row["Publisher"],
                "score": score
            })

    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)

    return recommendations[:5]
