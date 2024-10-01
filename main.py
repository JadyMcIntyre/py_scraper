import streamlit as st
from scrape import scrape_website

st.title("AI web scraper")

url = st.text_input("Enter a website url: ")

if st.button("Scrape site"):
    st.write("scraping the site")
    result = scrape_website(url)
    print(result)