from dataclasses import dataclass
import AmazonScraper

class Product:
    def get_data(self, new_webpage, new_soup) -> None:
        Amazon_Scraper = AmazonScraper.AmazonScraper(new_webpage, new_soup)
        self.name = Amazon_Scraper.get_name()
        self.price = Amazon_Scraper.get_price()
        self.rating = Amazon_Scraper.get_stars()
        self.number_of_reviews = Amazon_Scraper.get_rating()
        self.description = Amazon_Scraper.get_description()
        self.asin = Amazon_Scraper.get_asin()
        self.product_description = Amazon_Scraper.get_product_desc()
        self.manufacturer = Amazon_Scraper.get_manufacturer()
        