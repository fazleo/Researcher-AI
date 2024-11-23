import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os




# loading .env variables
load_dotenv() 
isOn = False
text = None


#configuring gemini api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])


#function to extract text from pdf paper
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()
    
    return text





def askGemini(query, text):
    response = chat.send_message([query, text])
    return response.text





# defining streamlit app interface

st.title("Researcher AI")
st.subheader("AI Research Paper Summarizer and Keypoint Extractor")



#receiving uploading file
uploaded_file = st.file_uploader("Upload a Reseach Paper (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting content from paper....."):
        try:
            text = extract_text_from_pdf(uploaded_file)
            # sample_pdf = genai.upload_file("./paper1.pdf")
            st.success("Text Extracted Succesfully")
        except:
            st.write("Error")
    




st.sidebar.subheader("Select the Task to perform ?")

taskOption = st.sidebar.radio(
    "Select From Below ",
    ["***Summarize***", "***Keypoints***", "***Table***", "***Similar Paper***"],
    captions=[
        "Summarize Paper.",
        "Extract Keypoints.",
        "Generate Review Table.",
        "Find Similar Papers."
    ],
)



st.text("")


submitButton = st.button("Submit", type="primary")

st.divider()







# Tokens: 21488
# Characters: 87570



if submitButton:
    # isOn = True
    if text != None:
        if taskOption == "***Summarize***":
            with st.spinner("Summarizing the paper..."):
    #    
                st.write("You selected Summary")
                prompt = "Summarize the following research paper. Provide a concise and clear summary highlighting the main points, including the research objective, methodology, key findings, and conclusions?"
                result = askGemini(prompt, text)
                st.write(result)

        if taskOption == "***Keypoints***":
            with st.spinner("Extracting Keypoints..."):
    #         
                st.write("Keypoints:")
                prompt = "Extract key points from the following research paper. Include the most important details about the research question, methodology, results, and implications in a bullet-point format?"
                result = askGemini(prompt, text)
                st.write(result)

        if taskOption == "***Table***":
            with st.spinner("Generating review table..."):
    #         
                st.write("Review Table:")

                prompt = """
                Generate a well-structured review table based on the content of the following research paper, not the paper specified in the literature review sections. The table should have the following columns:

            `        1. **Authors**: List the names of the author written research paper.
                    2. **Main Topic**: Summarize the main research topic or objective in one sentence.
                    3. **Compared Methodology**: Describe the methodologies from related work or references that are compared or reviewed in this paper.
                    4. **Proposed Methodology**: Briefly explain the methodology proposed by the authors.
                    5. **Results**: Summarize the key findings or results of the paper.
                    6. **Metrics Used**: List the evaluation metrics or criteria applied to analyze the results.

                    Ensure the table is formatted, and arrange table sideways consistently where sections are one below another. Provide clear, concise, and non-redundant entries for each column. If certain details are not available in the paper, leave the cell blank but include all relevant sections.
            `            """

                result = askGemini(prompt, text)
                st.write(result)
        
        if taskOption == "***Similar Paper***":
            with st.spinner("Finding similar papers..."):
    #         
                st.write("Similar Papers:")
                prompt = "Identify similar research papers based on the content provided below. List them with the title, authors, publication year, and a brief description of their relevance?"
                result = askGemini(prompt, text)
                st.write(result)

    else:
        st.write("Please upload a PDF file first.")


# st.text("History")

# chat_history = chat.history
# for i, message in enumerate(chat_history, start=1):
#     if message.role == "user":
#         st.write(f"Message: {i}")
#         st.write(f"User: {message.parts[0]}")
#     elif message.role == "model":
#         st.write(f"Assistant: {message.parts[0]}")
    
    