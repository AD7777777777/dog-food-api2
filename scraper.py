from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Debugging Route
@app.route('/')
def home():
    return "Dog Food API is running!"

# Comparison Route
@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    dog_size = data.get("size")
    weight = data.get("weight")
    age = data.get("age")

    brands = [
        {"brand": "Brand A", "ingredients": "Chicken, Rice, Carrots"},
        {"brand": "Brand B", "ingredients": "Beef, Oats, Peas"},
        {"brand": "Brand C", "ingredients": "Salmon, Sweet Potato, Flaxseed"},
    ]

    response = jsonify(brands)
    response.headers.add("Access-Control-Allow-Origin", "*")  # Enable CORS for all domains
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
