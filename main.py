import requests
from typing import List
import AmazonProduct
import AmazonScraper
import LinkScraper
from bs4 import BeautifulSoup


NO_PAGES = 20

HEADERS  = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}


try:
    File = open("out.csv", "a", encoding="utf-8")
except FileNotFoundError as e:
    print(e)
    
seen = set()

for i in range(1, NO_PAGES + 1):
    target_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}".format(i)
    resp =  requests.get(target_url, headers=HEADERS, timeout=60)
    Link_Scraper = LinkScraper.Link_Scraper(resp=resp)
    for link in Link_Scraper.get_links(resp):
        full_link = "https://www.amazon.in" + link
        try:
            new_webpage = requests.get(full_link, headers=HEADERS)
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        new_soup = BeautifulSoup(new_webpage.content, "lxml")
        product = AmazonProduct.Product()
        product.get_data(new_webpage, new_soup)
        scrape = f"{product.name},{product.price},{product.number_of_reviews},{product.rating},{product.description},{product.manufacturer},{product.product_description},{product.asin},{full_link},\n"
        if scrape in seen:
            continue
        seen.add(scrape)
        
        File.write(scrape)
        print(product.price)