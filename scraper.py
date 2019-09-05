import requests
from bs4 import BeautifulSoup
from datetime import datetime



class GisMeteoScraper:
    def __init__(self, gismeteo_address):
        self.gismeteo_address = gismeteo_address
        self.city = self.gismeteo_address.split("-")[1]
        self.date_of_scraping = None
        self._id = int()
        self.weather = dict()

    def scrape_info(self):
        try:
            page = requests.get(self.gismeteo_address, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(page.content, "html.parser")
            self.date_of_scraping = str(f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}")
            self._id = int(str(f"{datetime.today().day}{datetime.today().month}{datetime.today().year}"))
            times = soup.find("div", {"class": "widget__row widget__row_time"}).find_all("div", {"class": "w_time"})
            temperature = soup.find("div", {"class": "templine w_temperature"}).find_all("div", {"class": "value"})
            wind_speed = soup.find("div", {"class": "widget__row widget__row_table widget__row_wind-or-gust"}).find_all("div", {"class": "widget__item"})
            precipitation = soup.find("div", {"class": "widget__row widget__row_table widget__row_precipitation"}).find_all("div", {"class": "widget__item"})
            precipitation_in_r = soup.find("div", {"class": "widget__row widget__row_precipitationradius"}).find_all("div", {"class": "widget__value"})
            wind_direction = soup.find("div", {"class": "widget__row widget__row_table widget__row_wind"}).find_all("div", {"class": "w_wind__direction gray"})
            gusts = soup.find("div", {"class": "widget__row widget__row_table widget__row_gust"}).find_all("div", {"class": "widget__item"})
            road_condition = soup.find("div", {"class": "widget__row widget__row_roadcondition"}).find_all("div", {"class": "w_roadcondition__description"})
            pressure = soup.find("div", {"class": "widget__row widget__row_pressure"}).find_all("div", {"class": "value"})
            humidity = soup.find("div", {"class": "widget__row widget__row_table widget__row_humidity"}).find_all("div", {"class": "widget__item"})
            visibility = soup.find("div", {"class": "widget__row widget__row_table widget__row_visibility"}).find_all("div", {"class": "widget__item"})
            uvb_index = soup.find("div", {"class": "widget__row widget__row_table widget__row_uvb"}).find_all("div", {"class": "widget__item"})
            gm_activity = soup.find("div", {"class": "widget__row widget__row_table widget__row_gm"}).find_all("div", {"class": "widget__item"})
            _sun = soup.find("div", {"class": "astronomy_blocks clearfix"}).find_all("div", {"class": "astronomy_block _sun"})
            _moon = soup.find("div", {"class": "astronomy_blocks clearfix"}).find_all("div", {"class": "astronomy_block _moon"})
            
        except Exception as ex:
            raise ex
