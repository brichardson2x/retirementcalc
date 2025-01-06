from app import app
from flask import render_template, request, jsonify

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['POST']) # add methods=['POST']
def calculator():
    try:
        data = request.get_json
        print(data)
        print(request.headers)
        if not data:
            return jsonify({"message": "No data received"}), 400
        return jsonify({"message": "Data received", "data": data}), 200
    except Exception as e:
        app.logger.error(request.headers)
        app.logger.error(f"Is JSON: {request.is_json}")
        print(f"Error while decoding JSON: {e}")  # Logs the error to the console
        return jsonify({"error": f"Failed to decode JSON object: {str(e)}"}), 400





#    return jsonify({"message": "No data received"}), 200