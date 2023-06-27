import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the website to scrape
base_url = "https://www.bootcountryonline.com/collections/under-25?page="

# Maximum number of pages to scrape
max_pages = 10

# Create a CSV file to store the titles and prices
with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])

    # Iterate through the pages
    for page in range(1, max_pages + 1):
        url = base_url + str(page)

        # Make the HTTP request
        response = requests.get(url)

        # Create the BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all div elements with the class "grid-product__meta"
        product_meta_elements = soup.find_all('div', class_='grid-product__meta')

        # Iterate through the found elements
        for product_meta in product_meta_elements:
            # Extract the title of the product
            title = product_meta.find('div', class_='grid-product__title--heading').text.strip()

            # Extract the price of the product
            price = product_meta.find('div', class_='grid-product__price').text.strip()

            # Write the data to the CSV file
            writer.writerow([title, price])

print("The titles and prices of the products have been saved in 'products.csv'.")
