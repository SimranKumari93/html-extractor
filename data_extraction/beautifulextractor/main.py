from scrapper import (
     scrape_products_amazon,
     scrape_products_flipkart,
     scrape_products_myntra,
     aggregated_products,
)

def main():
    #URLs for scrapping 
    amazon_url = "https://www.amazon.com/"
    flipkart_url = "https://www.flipkart.com/"
    myntra_url = "https://www.myntra.com/"

    # scrapping data from different resources
    amazon_data = scrape_products_amazon(amazon_url)
    flipkart_data = scrape_products_flipkart(flipkart_url)
    myntra_data = scrape_products_myntra(myntra_url)

    # aggregating and duplicating data 
    aggregated_products = (amazon_data, flipkart_data, myntra_data)

         