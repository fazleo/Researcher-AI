import streamlit as st
import PyPDF2 as PdfReader
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os


# loading .env variables
load_dotenv() 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))