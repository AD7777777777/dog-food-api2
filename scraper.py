from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

# Function to scrape dog food data from a review website
def scrape_dog_food_data():
    url = "https://www.dogfoodadvisor.com/dog-food-reviews/"  # Example site
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    brands = []

    # Extract brand names and ingredients (modify based on actual site structure)
    for product in soup.select(".review-title"):  # Example selector
        brand_name = product.text.strip()
        ingredients = ", ".join([i.text.strip() for i in product.find_next("ul").select("li")])
        brands.append({"brand": brand_name, "ingredients": ingredients})

    return brands[:5]  # Get top 5 brands

# Route to process user input and return comparison data
@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    dog_size = data.get("size")
    weight = data.get("weight")
    age = data.get("age")

    # Get scraped data
    brands = scrape_dog_food_data()

    # Filter results based on ingredients (logic can be refined)
    filtered_brands = [
        brand for brand in brands if "chicken" in brand["ingredients"].lower()  # Example filtering
    ]

    return jsonify(filtered_brands)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
