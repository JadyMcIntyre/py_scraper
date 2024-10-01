import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.title("AI web scraper")

url = st.text_input("Enter a website url: ")

if st.button("Scrape site"):
    st.write("scraping the site")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    