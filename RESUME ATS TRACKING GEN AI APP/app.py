from dotenv import load_dotenv
load_dotenv()

import io
import os
import base64
import streamlit as st
from PIL import Image
from pdf2image import convert_from_bytes
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="")

# -------- GEMINI RESPONSE FUNCTION --------
def get_gemini_response(prompt, pdf_content, job_desc):
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    response = model.generate_content([
        prompt,
        job_desc,
        pdf_content[0]  # image part
    ])
    
    return response.text


from pdf2image import convert_from_bytes

def input_pdf_setup(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")

    images = convert_from_bytes(
        uploaded_file.read(),
        poppler_path=r"C:\Program Files (x86)\poppler-25.12.0\Library\bin"
    )

    first_page = images[0]

    img_byte_arr = io.BytesIO()
    first_page.save(img_byte_arr, format="JPEG")

    pdf_parts = [{
        "mime_type": "image/jpeg",
        "data": base64.b64encode(img_byte_arr.getvalue()).decode("utf-8")
    }]

    return pdf_parts



# -------- STREAMLIT UI --------
st.set_page_config(page_title="ATS Resume Expert")
st.header("📄 ATS Tracking System")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improve My Skills")
submit3 = st.button("Percentage Match")


# -------- PROMPTS --------
input_prompt1 = """
You are an experienced HR with strong technical expertise in Data Science,
Full Stack Web Development, Big Data Engineering, DevOps, and Data Analytics.

Analyze the provided resume against the job description.
Clearly explain:
- Profile alignment
- Strengths
- Weaknesses
- Hiring recommendation
"""

input_prompt3 = """
You are a highly accurate ATS (Applicant Tracking System) scanner.

Evaluate the resume against the job description.
Your output must be:
1. Percentage match
2. Missing keywords
3. Strengths
4. Improvement suggestions
"""


# -------- BUTTON LOGIC --------
if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("HR Evaluation")
        st.write(response)
    else:
        st.warning("Please upload a resume")

elif submit2:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Skill Improvement Suggestions")
        st.write(response)
    else:
        st.warning("Please upload a resume")

elif submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("ATS Percentage Match")
        st.write(response)
    else:
        st.warning("Please upload a resume")
