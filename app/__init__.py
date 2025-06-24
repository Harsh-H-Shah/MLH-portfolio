import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    work_experience = [
        {"role": "Software Developer Intern", "company": "Aumsat Technologies", "duration": "Jun 2023 – Oct 2023"},
        {"role": "Frontend Developer Intern", "company": "Skinzy Software", "duration": "Oct 2021 – Dec 2021"}
    ]

    education = [
        {"school": "Stony Brook University", "degree": "MS in Computer Science", "duration": "2024 – 2026"},
        {"school": "University of Mumbai - TSEC", "degree": "BE in Computer Engineering", "duration": "2020 – 2024"}
    ]
    return render_template('index.html', title="Harsh Shah", url=os.getenv("URL"), work_experience=work_experience, education=education)
