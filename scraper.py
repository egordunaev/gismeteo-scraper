from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import os
import logging
from datetime import datetime

db_address = os.environ.get("DB_ADDRESS", "")
db_port = 27017
client = MongoClient(db_address, db_port)
weather_db = client.weather

class GisMeteoScraper:
    def __init__(self, gismeteo_address, city):
        self.gismeteo_address = gismeteo_address
        self.city = city
        self.check_collection(self.city)
        self.scrape_info(self.gismeteo_address)
    
    def check_collection(self, city):
        try:
            if weather_db[city] is None:
                weather_db.create_collection(city)
                print(f"Collection {city} created")
                return
            print(f"Collection {city} exists")
        except Exception as ex:
            raise ex
    
    def scrape_info(self, address):
        try:
            page = requests.get(address, headers={"User-Agent":"Mozilla/5.0"})
            soup = BeautifulSoup(page.content, "html.parser")
            date_scraped = str(f"{datetime.today().day()}/{datetime.today().month()}/{datetime.today().year()}")
            return soup
        except Exception as ex:
            raise ex
