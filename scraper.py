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
            self.weather = {"id": self._id, "date": self.date_of_scraping, "city": self.city}
            times = soup.find("div", {"class": "widget__row widget__row_time"}).find_all("div", {"class": "w_time"})
            time_dict = dict()
            iterator = 0
            for item in times:
                time_dict.update({item.contents[0].contents[0]: {"id": iterator}})
                iterator += 1
            for item in time_dict:
                time_dict[item].update({"temperature": self.get_temperature(soup, time_dict[item]["id"]),
                                        "wind": {"speed": self.get_wind_speed(soup, time_dict[item]["id"]),
                                                 "direction": self.get_wind_direction(soup, time_dict[item]["id"]),
                                                 "gust": self.get_gusts(soup, time_dict[item]["id"])},
                                        "percipitation": self.get_precipitation(soup, time_dict[item]["id"]),
                                        "percipitation_in_radius": self.get_precipitation_in_radius(soup, time_dict[item]["id"]),
                                        "road_condition": self.get_road_condition(soup, time_dict[item]["id"]),
                                        "pressure": self.get_pressure(soup, time_dict[item]["id"]),
                                        "humidity": self.get_humidity(soup, time_dict[item]["id"]),
                                        "visibility": self.get_visibility(soup, time_dict[item]["id"]),
                                        "uvb_index": self.get_uvb(soup, time_dict[item]["id"]),
                                        "gm_activity": self.get_gm_activity(soup, time_dict[item]["id"]),
                                        "sun": self.get_sun_info(soup, time_dict[item]["id"]),
                                        "moon": self.get_moon_info(soup, time_dict[item]["id"])})
            
            self.weather.update(time_dict)
            return self.weather
        except Exception as ex:
            raise ex

    def get_temperature(self, soup, time_id):
        try:
            temperature_soup = soup.find("div", {"class": "templine w_temperature"}).find_all("div", {"class": "value"})
            temperature = {"celsius": temperature_soup[time_id].contents[0].contents[0],
                           "fahrenheit": temperature_soup[time_id].contents[1].contents[0]}
            return temperature
        except Exception as ex:
            raise ex

    def get_wind_speed(self, soup, time_id):
        try:
            wind_speed_soup = soup.find("div", {"class": "widget__row widget__row_table widget__row_wind-or-gust"}).find_all("div", {"class": "widget__item"})
            wind_speed = {"m/s": wind_speed_soup[time_id].contents[0].contents[0].contents[1].contents[0].strip(),
                          "mi/h": wind_speed_soup[time_id].contents[0].contents[0].contents[2].contents[0].strip(),
                          "km/h": wind_speed_soup[time_id].contents[0].contents[0].contents[3].contents[0].strip()}
            return wind_speed
        except Exception as ex:
            raise ex

    def get_wind_direction(self, soup, time_id):
        try:
            wind_direction = soup.find("div", {"class": "widget__row widget__row_table widget__row_wind"}).find_all("div", {"class": "w_wind__direction gray"})
            direction = wind_direction[time_id].contents[0].strip()
            return direction
        except Exception as ex:
            raise ex

    def get_gusts(self, soup, time_id):
        try:
            gusts = soup.find("div", {"class": "widget__row widget__row_table widget__row_gust"}).find_all("div", {"class": "widget__item"})
            gust = {"m/s": gusts[time_id].contents[0].contents[0].contents[1].contents[0].strip(),
                    "mi/h": gusts[time_id].contents[0].contents[0].contents[2].contents[0].strip(),
                    "km/h": gusts[time_id].contents[0].contents[0].contents[3].contents[0].strip()}
            return gust
        except Exception:
            return "No info"
    
    def get_precipitation(self, soup, time_id):
        try:
            precipitation_soup = soup.find("div", {"class": "widget__row widget__row_table widget__row_precipitation"}).find_all("div", {"class": "widget__item"})
            precipitation = precipitation_soup[time_id].contents[0].contents[0].contents[0]
            return precipitation
        except Exception:
            return "Without precipitation"
    
    def get_precipitation_in_radius(self, soup, time_id):
        try:
            precipitation_in_r = soup.find("div", {"class": "widget__row widget__row_precipitationradius"}).find_all("div", {"class": "widget__value"})
            precipitation = precipitation_in_r[time_id].contents[1].contents[0].contents[0]
            return precipitation
        except Exception:
            try:
                precipitation_in_r = soup.find("div", {"class": "widget__row widget__row_precipitationradius"}).find_all("div", {"class": "widget__value"})
                precipitation = precipitation_in_r[time_id].contents[1].contents[0].strip()
                return precipitation
            except Exception:
                return "No info"
    
    def get_road_condition(self, soup, time_id):
        try:
            road_condition_soup = soup.find("div", {"class": "widget__row widget__row_roadcondition"}).find_all("div", {"class": "w_roadcondition__description"})
            road_condition = road_condition_soup[time_id].contents[0]
            return road_condition
        except Exception:
            return "No info"
    
    def get_pressure(self, soup, time_id):
        try:
            pressure_soup = soup.find("div", {"class": "widget__row widget__row_pressure"}).find_all("div", {"class": "value"})
            pressure = {"mm_hg_atm": pressure_soup[time_id].contents[0].contents[0],
                        "h_pa": pressure_soup[time_id].contents[1].contents[0],
                        "in_hg": pressure_soup[time_id].contents[2].contents[0]}
            return pressure
        except Exception as ex:
            raise ex
    
    def get_humidity(self, soup, time_id):
        try:
            humidity_soup = soup.find("div", {"class": "widget__row widget__row_table widget__row_humidity"}).find_all("div", {"class": "widget__item"})
            humidity = humidity_soup[time_id].contents[0].contents[0]
            return humidity
        except Exception as ex:
            raise ex
    
    def get_visibility(self, soup, time_id):
        try:
            visibility_soup = soup.find("div", {"class": "widget__row widget__row_table widget__row_visibility"}).find_all("div", {"class": "widget__item"})
            visibility = visibility_soup[time_id].contents[0].contents[0].contents[0].strip()
            return visibility
        except Exception as ex:
            raise ex
    
    def get_uvb(self, soup, time_id):
        try:
            uvb_soup = soup.find("div", {"class": "widget__row widget__row_table widget__row_uvb"}).find_all("div", {"class": "widget__item"})
            uvb_value = int(uvb_soup[time_id].contents[0].contents[0])
            if uvb_value >= 0 and uvb_value <= 4:
                uvb_description = "Small disturbances"
            if uvb_value == 5:
                uvb_description = "Minor storm"
            if uvb_value == 6:
                uvb_description = "Moderate storm"
            if uvb_value == 7:
                uvb_description = "Strong storm"
            if uvb_value == 8:
                uvb_description = "Storm"
            if uvb_value == 9:
                uvb_description = "Extreme storm"
            uvb = {"value": uvb_value, "description": uvb_description}
            return uvb
        except Exception:
            uvb_value = uvb_soup[time_id].contents[0].contents[0]
            return {"value": uvb_value, "description": ""}
    
    def get_gm_activity(self, soup, time_id):
        try:
            gm_activity_soup = soup.find("div", {"class": "widget__row widget__row_table widget__row_gm"}).find_all("div", {"class": "widget__item"})
            gm_value = int(gm_activity_soup[time_id].contents[0].contents[0])
            if gm_value >= 0 and gm_value <= 4:
                gm_description = "Small disturbances"
            if gm_value == 5:
                gm_description = "Minor storm"
            if gm_value == 6:
                gm_description = "Moderate storm"
            if gm_value == 7:
                gm_description = "Strong storm"
            if gm_value == 8:
                gm_description = "Storm"
            if gm_value == 9:
                gm_description = "Extreme storm"
            gm_activity = {"value": gm_value, "description": gm_description}
            return gm_activity
        except Exception:
            gm_value = gm_activity_soup[time_id].contents[0].contents[0]
            return {"value": gm_value, "description": ""}
    
    def get_sun_info(self, soup, time_id):
        try:
            sun_soup = soup.find("div", {"class": "astronomy_block _sun"}).find_all("div", {"class": "ii info_detail"})
            sun_soup_description = soup.find("div", {"class": "astronomy_blocks clearfix"}).find_all("div", {"class": "astronomy_block _sun"})
            sun = {"title": sun_soup[0].contents[1].contents[0],
                   "sunrise": sun_soup[0].contents[3].contents[0].split(" — ")[1],
                   "sunset": sun_soup[0].contents[5].contents[0].split(" — ")[1],
                   "description": sun_soup_description[0].contents[5].contents[1].contents[0].strip()}
            return sun
        except Exception as ex:
            raise ex
    
    def get_moon_info(self, soup, time_id):
        try:
            moon_soup = soup.find("div", {"class": "astronomy_block _moon"}).find_all("div", {"class": "ii info_detail"})
            moon_soup_description = soup.find("div", {"class": "astronomy_blocks clearfix"}).find_all("div", {"class": "astronomy_block _moon"})
            moon = {"title": moon_soup[0].contents[1].contents[0].strip(),
                    "sunrise": moon_soup[0].contents[3].contents[0].split(" — ")[1],
                    "sunset": moon_soup[0].contents[5].contents[0].split(" — ")[1],
                    "description": moon_soup_description[0].contents[5].contents[1].contents[0].strip()}
            return moon
        except Exception as ex:
            raise ex
