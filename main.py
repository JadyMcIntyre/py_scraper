import streamlit as st

st.title("AI web scraper")

url = st.text_input("Enter a website url: ")

if st.button("Scrape site"):
    st.write("scraping the site")