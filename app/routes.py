from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator') # add methods=['POST']
def calculator():
    return render_template('test.html')
