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

@app.route("/travel")
def travel():
    return render_template("travel.html", title="Harsh Shah")

@app.route("/hobbies")
def hobbies():
    hobbies = [
        {
            "name": "Photography", 
            "image": "img/photography.jpg",
            "icon": "📸",
            "description": "Capturing moments and exploring the world through my lens. I love street photography and nature shots."
        },
        {
            "name": "Gaming", 
            "image": "img/gaming.jpg",
            "icon": "🎮",
            "description": "Strategic thinking and problem-solving through competitive gaming. Favorite genres include strategy and RPGs."
        },
        {
            "name": "Traveling", 
            "image": "img/traveling.jpg",
            "icon": "✈️",
            "description": "Exploring new cultures, cuisines, and landscapes. Every journey brings new perspectives and experiences."
        }
    ]
    return render_template("hobbies.html", title="Harsh Shah", hobbies=hobbies)
