import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import MySQLDatabase, SqliteDatabase
from peewee import Model, CharField, TextField, DateTimeField
from playhouse.shortcuts import model_to_dict
import datetime

load_dotenv()
app = Flask(__name__)

# Decide which DB to use *before* connecting
if os.getenv("TESTING") == "true":
    print("Running in test mode with SQLite in-memory DB")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

# Connect & create tables
mydb.connect()
mydb.create_tables([TimelinePost])

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

@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Harsh Shah")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    content = request.form.get('content', '').strip()
    
    if not name:
        return "Invalid name", 400
    if not content:
        return "Invalid content", 400
    if not email or '@' not in email:
        return "Invalid email", 400
    
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    try:
        post = TimelinePost.get_by_id(post_id)
        post.delete_instance()
        return {'message': f'Timeline post {post_id} deleted successfully'}
    except TimelinePost.DoesNotExist:
        return {'error': f'Timeline post {post_id} not found'}, 404
