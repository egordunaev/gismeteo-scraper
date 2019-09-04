import requests
from bs4 import BeautifulSoup
from datetime import datetime



class GisMeteoScraper:
    def __init__(self, gismeteo_address):
        self.gismeteo_address = gismeteo_address
        self.city = self.gismeteo_address.split("-")[1]
        self.date_of_scraping = None
        self.weather = dict()

    def scrape_info(self):
        try:
            page = requests.get(self.gismeteo_address, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(page.content, "html.parser")
            self.date_of_scraping = str(f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}")
            return soup
        except Exception as ex:
            raise ex
