import requests
from bs4 import BeautifulSoup
import csv
import os

url = "https://www.nike.com/w/best-76m50"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
products = soup.find_all("div", class_="product-card__body")

data = []
processed_products = {}

for product in products:
    name = product.find("a", class_="product-card__link-overlay").text.strip()
    if name in processed_products:
        continue  # Skip the product if it has already been processed
    
    processed_products[name] = True  # Mark the product as processed
    
    price = product.find("div", class_="product-price").text.strip()

    discount_element = product.find("div", class_="product-price us__styling is--striked-out css-0")
    if discount_element:
        discount_text = discount_element.text.strip()
        if "$" in discount_text:
            d_price = discount_text.split("$")
            o_price = price.split("$")
            original_price = float(d_price[1])
            discounted_price = float(o_price[1])
            if original_price != 0:
                discount_percentage = round((1 - discounted_price / original_price) * 100, 2)
                discount = f"{int(discount_percentage)}% off"
            else:
                discount = "Invalid discount"
        else:
            discount = discount_text
    else:
        discount = "No discount"

    data.append([name, price, discount])

# Create the 'data' directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save the scraped data to a CSV file in the 'data' directory
with open("data/nike_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Discount"])
    writer.writerows(data)

print("Scraping completed.")