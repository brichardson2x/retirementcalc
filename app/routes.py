from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['POST'])
def calculator():
    ###