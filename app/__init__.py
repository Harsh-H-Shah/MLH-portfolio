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
    travel_destinations = [
        {
            "name": "Tokyo, Japan",
            "flag": "🇯🇵",
            "image": "img/tokyo.jpg",
            "date": "March 2023",
            "description": "An incredible blend of traditional culture and cutting-edge technology. From serene temples to bustling Shibuya crossing.",
            "highlights": ["Sushi", "Cherry Blossoms", "Technology", "Culture"]
        },
        {
            "name": "Paris, France",
            "flag": "🇫🇷",
            "image": "img/paris.jpg",
            "date": "July 2022",
            "description": "The city of lights and romance. Amazing architecture, world-class museums, and incredible French cuisine.",
            "highlights": ["Eiffel Tower", "Louvre", "Cuisine", "Architecture"]
        },
        {
            "name": "Mumbai, India",
            "flag": "🇮🇳",
            "image": "img/mumbai.jpg",
            "date": "Home",
            "description": "My home city - a vibrant metropolis where dreams come alive. From street food to Bollywood, it's the heart of India.",
            "highlights": ["Street Food", "Bollywood", "Marine Drive", "Culture"]
        }
    ]
    
    travel_stats = {
        "countries": "5+",
        "cities": "15+",
        "continents": "3",
        "photos": "1000+"
    }
    
    return render_template("travel.html", title="Harsh Shah", travel_destinations=travel_destinations, travel_stats=travel_stats)
