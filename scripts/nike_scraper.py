import requests
from bs4 import BeautifulSoup
import csv
import os
import re

url = "https://www.nike.com/w/best-76m50"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
products = soup.find_all("div", class_="product-card__body")

data = []
processed_products = {}

for product in products:
    a_tag = product.find("a", class_="product-card__link-overlay")
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
    print(name) # Scraper takes a while to process so this is here to show it's working
    # Gets ratings from each product link
    prod_link = a_tag['href'] if a_tag else 'No link found'
    response2 = requests.get(prod_link)
    link_content = response2.text
    soup2 = BeautifulSoup(link_content, "html.parser")
    
    rating_element = soup2.find('div', class_='css-n209rx')
    rating = rating_element['aria-label'] if rating_element and 'aria-label' in rating_element.attrs else "No aria-label found"
    print(rating)

    # Gets number of reviews from each product link
    reviews_string = soup2.find("summary", class_="css-rptnlm").text.strip()
    num_reviews = re.search(r'Reviews \((\d+)\)', reviews_string)
    reviews = num_reviews.group(1)

    description = soup2.find("div", class_="description-preview body-2 css-1pbvugb").text.strip()

    data.append([name, price, discount, rating, reviews, description])

# Create the 'data' directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save the scraped data to a CSV file in the 'data' directory
with open("data/nike_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Discount", "Rating", "Reviews", "Description"])
    writer.writerows(data)

print("Scraping completed.")