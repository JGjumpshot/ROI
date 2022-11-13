from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
contact_types = ['Chat', 'Email', 'Phone', 'Other']
languages_tab_1 = ['English','French', 'Spanish', 'Portuguese', 'Polish', 'Turkish', 'Czech']
languages_tab_2 = ['Dutch', 'Norwegian', 'Swedish', 'Finnish', 'German', 'Danish', 'French Canadian']
languages_tab_3 = ['Russian', 'Arabic', 'Hindi', 'Romanian', 'Hungarian', 'Mandarin', 'Greek Italian']
industries = ['Technology', 'Healthcare', 'Retail / E-commerce', 'Financial Education', 'Education', 'Business', 'Real Estate', 'Automotive', 'Government']

@app.route('/')
def home():
    title = "Welcome"
    return render_template("home.html", title=title)

@app.route('/support')
def support():
    title="Get Started"
    return render_template("support.html", title=title, len = len(contact_types), contact_types=contact_types, lenl1=len(languages_tab_1), languages_tab_1=languages_tab_1, lenl2=len(languages_tab_2), languages_tab_2=languages_tab_2, lenl3= len(languages_tab_3), languages_tab_3=languages_tab_3, leni=len(industries), industries=industries)

@app.route('/submit', methods=['POST'])
def submit():
    title="Submit"
    print(request.data)

    return render_template('submit.html', title=title)