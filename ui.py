import streamlit as st
from scrape import scrape_website
from llm import ChatModel

def start_streamlit_app(**kwargs):

    chrome_driver_path = kwargs.get('chrome_driver_path')
    chunk_size = kwargs.get('chunk_size')
    gemini_api_key = kwargs.get('gemini_api_key')

    searchModel = ChatModel(gemini_api_key)

    st.title('AI Web Scraper Tool')

    url = st.text_input('Enter the URL to scrape')

    if st.button('Scrape'):
        st.write('Scraping...')
        print("Starting scraping...")
        scrape_website_result = scrape_website(url, chrome_driver_path)
        st.session_state.dom_content = scrape_website_result

        with st.expander('View Scraped Content'):
            st.text_area("Scraped Content:", scrape_website_result, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("Describe what you want to parse")

        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing the content...")
                parsed_result = searchModel.get_document_contents(st.session_state.dom_content, parse_description, chunk_size)
                st.write(parsed_result)