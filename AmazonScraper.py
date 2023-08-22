from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from typing import List

@dataclass
class AmazonScraper:
    resp: requests.Response
    soup: BeautifulSoup

    def get_price(self) -> str:
        price = ""
        try:
            price = self.soup.find("span", attrs={'class':'a-price-whole'}).text.strip()
        except Exception as e:
            return "NA"
        price = price.replace(",", ".")
        if price.endswith("."):
            price = price[:-1]
        return price

    def get_name(self) -> str:
        product_name = ""
        try:
            product_name: str = self.soup.find('span', {"id" : "productTitle"}).text.strip()
        except Exception as e:
            return "NA"
        product_name = product_name.replace(",", ".")
        return product_name
    def get_rating(self) -> str:
        ratings: str = ""
        try:
            ratings = self.soup.find('span', {"id" : "acrCustomerReviewText"}).text.strip()
        except Exception as e:
            return "NA"
        ratings = ratings.replace(",", ".")
        return ratings
    def get_stars(self) -> str:
        stars: str = ""
        try:
            stars = self.soup.find('span', {'class' : 'a-icon-alt'}).text.strip()
        except Exception as e:
            return "NA"
        return stars
    def get_description(self) -> str:
        desc: str = ""
        try:
            desc = self.soup.find('meta', {'name' : 'description'}).get('content')
            desc.join("\n")
        except Exception as e:
            return "NA"
        desc = desc.replace(",", ".")
        return desc
    def get_asin(self) -> str:
        
        link = self.resp.url
        tmp: str = ""
        asin: str = ""
        try:
            tmp = link.split("dp/")
            asin = tmp[1]
            asin = asin.split("/")
        except Exception as e:
            return "NA"
        return asin[0]
    def get_product_desc(self) -> str:
        desc: List[str] = []
        try:
            tmp = self.soup.find('ul', {'class' : 'a-unordered-list a-vertical a-spacing-mini'})
            size = len(tmp.find_all('span', {'class' : 'a-list-item'}))
            tmp = tmp.find('span', {'class' : 'a-list-item'})
            for _ in range(size):
                desc.append(tmp.text.strip())
                tmp = tmp.find_next('span', {'class' : 'a-list-item'})                
        except Exception as e:
            print(e)
            return ""
        return " ".join(desc)
    def get_manufacturer(self) -> str:
        manufacturer: str = ""
        try:
            manufacturer = self.soup.find('img', {'class' : 'brand-snapshot-badge-space'})
            manufacturer = manufacturer.find_next()
            manufacturer = manufacturer.find("span", {'class' : 'a-size-medium a-text-bold'}).text.strip()
        except Exception as e:
            return "NA"
        return manufacturer