# Task 11
# Deploy the trained model using a simple web interface with either Flask or Streamlit and allow users to enter a news article and obtain the predicted category in real time.
import joblib
import streamlit as st

model=joblib.load('model.joblib')

st.set_page_config(page_title="News Categorizer")
st.title("News Categorizer")
st.caption("TF-IDF + Naive Bayes — BBC News Dataset")
st.divider()
article = st.text_area("Paste your news article here : ",height=200)

if st.button("Classify",use_container_width=True):
    if article.strip() == "":
        st.warning("Please Enter the article first")
    else:
        prediction = model.predict([article])[0]
        st.success(f"*Category: {prediction}*")