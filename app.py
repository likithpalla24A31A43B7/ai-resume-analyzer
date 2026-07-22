import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

st.title("AI Resume Analyzer")

skills = [
    "Python",
    "SQL",
    "Power BI",
    "Machine Learning",
    "Java",
    "Excel",
    "Pandas",
    "Data Analysis"
]

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)

text = ""

if uploaded_file is not None:

    # Read PDF files
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    # Read DOCX files
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    st.subheader("Skills Found")

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    if found_skills:
        for skill in found_skills:
            st.write(f"✅ {skill}")
    else:
        st.write("No matching skills found.")
        score = (len(found_skills) / len(skills)) * 100

score = (len(found_skills) / len(skills)) * 100

st.subheader("Resume Score")
st.progress(int(score))
st.write(f"Score: {score:.0f}/100")
st.subheader("Recommended Skills")

for skill in skills:
    if skill not in found_skills:
        st.write(f"❌ {skill}")