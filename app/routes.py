from app import app
from flask import render_template, request, jsonify

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['POST']) # add methods=['POST']
def calculator():

    return '', 200