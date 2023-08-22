from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests

@dataclass
class Link_Scraper:
    resp: requests.Response
    
    def get_links(self, soup) -> set[str]:
        soup = BeautifulSoup(self.resp.text, "lxml")
        try: 
            links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        except:
            return set()
        links_list: set[str] = set()

        for link in links:
            links_list.add(link.get('href'))
        return links_list
