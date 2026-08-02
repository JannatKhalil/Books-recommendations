import streamlit as st
import joblib
from recommendation import recommend

# Load data
df = joblib.load("models/books.pkl")

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp{
    background: linear-gradient(-45deg,#000000,#081229,#0b3d91,#000000);
    background-size:400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Hide Streamlit Menu & Footer */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.title{
    text-align:center;
    color:#00BFFF;
    font-size:55px;
    font-weight:bold;
    text-shadow:0px 0px 20px #00BFFF;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:white;
    font-size:20px;
    margin-bottom:30px;
}

/* Button */
div.stButton > button{
    background:#00BFFF;
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    width:230px;
    font-size:20px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:#007BFF;
    transform:scale(1.05);
    transition:0.3s;
}

/* Recommendation Card */
.card{
    background:#111827;
    border-left:6px solid #00BFFF;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
    box-shadow:0px 0px 20px rgba(0,191,255,.35);
}

/* Footer */
.footer{
    text-align:center;
    color:#9CA3AF;
    margin-top:40px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("📚 AI Book Recommender")

    st.write("---")

    st.write("""
### About

This project recommends books using:

- 📚 Machine Learning
- 🧠 TF-IDF Vectorizer
- 📊 Cosine Similarity
- 🐍 Python
- ⚡ Streamlit

Simply select a book and click the button.
""")

    st.write("---")

    st.success(" Thank you ❤️ ")

# ---------------- TITLE ---------------- #

st.markdown(
'<div class="title">📚 AI Book Recommendation System</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Discover your next favorite book with Artificial Intelligence ✨</div>',
unsafe_allow_html=True
)

# ---------------- SELECT BOOK ---------------- #

book_name = st.selectbox(
    "📖 Select a Book",
    sorted(df["Title"].unique())
)

# ---------------- BUTTON ---------------- #

if st.button("🚀 Recommend Books"):

    books = recommend(book_name)

    st.subheader("⭐ Recommended Books")

    for book in books:

        details = df[df["Title"] == book]

        if not details.empty:

            st.markdown(f"""
<div class="card">

<h3 style="color:#00BFFF;">📖 {book}</h3>

<b>✍ Author:</b> {details.iloc[0]['Author']}<br><br>

<b>⭐ Rating:</b> {details.iloc[0]['Rating']}<br><br>

<b>📚 Genres:</b> {details.iloc[0]['Genres']}

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #

st.markdown(
'<div class="footer"> </div>',
unsafe_allow_html=True
)