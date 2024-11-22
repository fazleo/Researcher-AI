import streamlit as st
import PyPDF2 as PdfReader
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os


# loading .env variables
load_dotenv() 


#configuring gemini api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
print(os.getenv("GOOGLE_API_KEY"))

#function to extract text from pdf paper
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text




# defining streamlit app interface

st.title("Researcher AI")
st.subheader("AI Research Paper Summarizer and Keypoint Extractor")



#receiving uploading file
uploaded_file = st.file_uploader("Upload a Reseach Paper (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting content from paper....."):
        text = extract_text_from_pdf(uploaded_file)
    st.success("Text Extracted Succesfully")


summarizeButton = st.sidebar.button("Summarize Paper")
keypointButton = st.sidebar.button("Extract Keypoints")
reviewButton = st.sidebar.button("Generate Review Table")
similarButton = st.sidebar.button("Find Similar Papers")



if summarizeButton:
    with st.spinner("Summarizing the paper..."):
        st.write("Summary of Paper: \n -------content-------")


submitButton = st.button("Submit", type="primary")

st.divider()

st.text("History")