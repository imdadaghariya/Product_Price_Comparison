import requests
from bs4 import BeautifulSoup

def scrape_product_prices(product_name):
    # List of target URLs to scrape
    urls = [
        'https://www.flipkart.com',
        'https://www.amazon.in',
        'https://www.samsung.com/in'
    ]

    prices = []

    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant elements containing product information
        product_elements = soup.find_all('div', class_='product')

        for product_element in product_elements:
            # Extract the product name and price from the element
            name = product_element.find('h2').text.strip()
            price = product_element.find('span', class_='price').text.strip()

            # Check if the product name matches the desired product
            if product_name.lower() in name.lower():
                # Add the price to the list
                prices.append({'Website': url, 'Name': name, 'Price': price})

    return prices

# Example usage
product_name = 'samsung s23 ultra'
results = scrape_product_prices(product_name)

# Print the scraped prices
for result in results:
    print(f"Website: {result['Website']}")
    print(f"Product: {result['Name']}")
    print(f"Price: {result['Price']}")
    print()
