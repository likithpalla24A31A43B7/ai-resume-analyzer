# AI Resume Analyzer

## Overview

AI Resume Analyzer is a Python-based application that analyzes resumes and extracts important skills automatically. The application supports both PDF and DOCX resume formats and provides a resume score based on detected skills.

## Features

* Upload PDF resumes
* Upload DOCX resumes
* Extract text from resumes automatically
* Detect technical skills from resume content
* Generate a resume score
* Recommend missing skills for improvement

## Technologies Used

* Python
* Streamlit
* PyPDF2
* python-docx
* Pandas

## Supported Resume Formats

* PDF (.pdf)
* Microsoft Word Document (.docx)

## Skills Detection

The application currently detects the following skills:

* Python
* SQL
* Power BI
* Machine Learning
* Java
* Excel
* Pandas
* Data Analysis

## How It Works

1. Upload a resume file.
2. The application extracts text from the document.
3. The extracted text is analyzed for predefined technical skills.
4. Detected skills are displayed.
5. A resume score is calculated based on the number of matching skills.
6. Missing skills are suggested for improvement.

## Project Structure

resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf

## Installation

Install the required libraries:

pip install streamlit pandas PyPDF2 python-docx

Run the application:

python -m streamlit run app.py

## Future Improvements

* Job description matching
* AI-based skill recommendations
* Resume ranking system
* ATS compatibility checking
* Interactive dashboard and analytics

## Author

Developed as an AI project for learning Natural Language Processing and document analysis using Python.
