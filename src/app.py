import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

from agents.blogpostcreator import BlogPostCreator

with st.sidebar:
    "## Blog Post Generator"

    "### How to use"

    """
    1. Enter the number of web references you want to use. (Max 10).
    2. Enter the keyword you want to generate a blog post for.
    3. Click on the "Generate blog post" button.
    """
            
    web_references = st.number_input(
        label="Enter number of web references to use",
        max_value=10,
        min_value=1,
        value=3,
    )

    st.divider()

    """
    ### About

    Blog Post Generator allows you to generate an SEO optimised blog post from keywords. 
    It uses web references from top ranking articles to generate your blog post. 
    It also allows you to specify a number of web links to use. 
    It only allows a maximum of 10.
    """
    st.divider()


st.title("Blog Post Generator ")

with st.form(key="generate_blog_post"):
    keyword = st.text_input(label= "Enter a keyword", placeholder="")

    submitted = st.form_submit_button("Generate blog post")
    
if submitted and not openai_api_key:
        st.info("Please enter your OpenAI API key", icon="ℹ️")
        
elif submitted and not keyword:
        st.warning("Please enter a keyword", icon="⚠️")
        
elif submitted:
    creator = BlogPostCreator(keyword, web_references)       
    response = creator.create_blog_post()

    if response is None or not response:
          st.status("Generating ... ")    
    elif isinstance(response, Exception):
            st.warning("An error occured. Please try again!")
            st.error(response, icon="🚨")
    
    else:
            st.write("### Generated blog post")
            st.write(response)
            st.snow()

