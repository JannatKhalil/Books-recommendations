import joblib

# Load saved files
df = joblib.load("models/books.pkl")
similarity = joblib.load("models/recommender.pkl")


def recommend(book_name):
    if book_name not in df["Title"].values:
        return ["Book not found"]

    index = df[df["Title"] == book_name].index[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended_books = []

    for i in distances[1:6]:
        recommended_books.append(df.iloc[i[0]]["Title"])

    return recommended_books