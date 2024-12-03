import streamlit as st
from streamlit.logger import get_logger

st.set_page_config(
    page_title="Welcome Screen",
    page_icon="👋",
)


st.markdown("<h1 style='text-align: center; color: white;'>Book Recommendation Engine</h1>", unsafe_allow_html=True)
st.image("img/library_img.jpg", caption="Welcome to Book Recommendation App")
st.write("The world of books is vast, and readers often seek personalized recommendations to discover new titles that align with their interests. This project aims to create a book recommendation system that considers user preferences, reading history, and book attributes to provide tailored book recommendations.")


