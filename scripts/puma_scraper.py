import requests
from bs4 import BeautifulSoup
import csv
import os

url = "https://us.puma.com/us/en/puma/shop-all-classics/best-selling-classics"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
products = soup.find_all("div", class_="relative w-full flex flex-col gap-2")

data = []
processed_products = {}

for product in products:
    name_element = product.find("h3", class_="w-full mobile:text-sm mobile:pr-0 font-bold text-base pr-5 line-clamp-2")
    
    color_element = product.find("span", class_="sr-only")
    if color_element:
        color = color_element.text.strip()
        color_element.decompose()  # Remove the color span from the name element
    else:
        color = "N/A"
    
    name = name_element.text.strip()
    # if name in processed_products:
    #     continue  # Skip the product if it has already been processed
    
    # processed_products[name] = True  # Mark the product as processed

    price = product.find("div", class_="flex flex-col flex-none mobile:items-start items-end text-sm md:text-base mobile:mt-2").text.strip()
    
    discount_element = product.find("span", class_="whitespace-nowrap text-base line-through opacity-50 override:text-puma-black-300 override:opacity-100")
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
                price = discounted_price
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
with open("data/puma_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Discount"])
    writer.writerows(data)

print("Scraping completed.")