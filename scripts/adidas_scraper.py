import requests
from bs4 import BeautifulSoup
import csv
import os
import time

url = "https://www.adidas.com/us/men-shoes"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
products = soup.find_all("div", class_="gl-product-card")

data = []
for product in products:
    name = product.find("div", class_="gl-product-card__name").text.strip()
    price = product.find("div", class_="gl-product-card__price").text.strip()
    data.append([name, price])
    print(f"Scraped: {name} - {price}")
    time.sleep(1)  # Delay for 1 second between requests

# Create the 'data' directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save the scraped data to a CSV file in the 'data' directory
with open("data/adidas_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price"])
    writer.writerows(data)

print("Scraping completed.")