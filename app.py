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
    return render_template("home.html", title=title)

@app.route('/support')
def support():
    title="Get Started"
    return render_template("support.html", title=title)

@app.route('/submit', methods=['POST'])
def submit():
    title="Submit"
    print(request.data)

    return render_template('submit.html', title=title)