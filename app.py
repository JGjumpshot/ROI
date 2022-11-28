from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import os
import json
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
    email = ''
    phone = ''
    return render_template("support.html", title=title, len = len(contact_types), contact_types=contact_types, lenl1=len(languages_tab_1), languages_tab_1=languages_tab_1, lenl2=len(languages_tab_2), languages_tab_2=languages_tab_2, lenl3= len(languages_tab_3), languages_tab_3=languages_tab_3, leni=len(industries), industries=industries, email=email, phone=phone)

@app.route('/submit', methods=['POST'])
def submit():
    title="Submit"
    contact_needs = request.form.getlist('contact_checkbox')
    language1_needs = request.form.getlist('lang1_checkbox')
    language2_needs = request.form.getlist('lang2_checkbox')
    language3_needs = request.form.getlist('lang3_checkbox')
    message = "Thank you! We plan on contacting you soon!"
    email = request.form.get('email')
    phone = request.form.get('phone')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, email, message)
    print([contact_needs, language1_needs, language2_needs, language3_needs, email, phone])

    return render_template('submit.html', title=title)