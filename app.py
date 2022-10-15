from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

@app.route('/')
def home():
    title = "Welcome"
    return render_template("index.html", title=title)