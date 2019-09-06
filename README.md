# GisMeteoScraper

This is a python web scraper for [gismeteo.com](gismeteo.com), it scrapes all html content from webpage and


### Requirements

GisMeteoScraper uses libraries such as:
* requests
* bs4 (BeautifulSoup4)

### Usage example

    from scraper import GisMeteoScraper
    
    gis = GisMeteoScraper("link to gismeteo with town")
    weather = gis.scrape_info()


### Output
GisMeteoScraper's `scrape_info()` outputs `dict()` object, which contains weather on each timeslot *(like `0`, or `21`)*, for example:

    'timeslot': 
    {'gm_activity': {
		    'description': '', 
		    'value': },
     'humidity': '',
       'id': ,
       'moon': {'description': '',
                'sunrise': '',
                'sunset': '',
                'title': ''},
       'percipitation': '',
       'percipitation_in_radius': '',
       'pressure': {
		       'h_pa': '', 
		       'in_hg': '', 
		       'mm_hg_atm': ''},
       'road_condition': '',
       'sun': {
		   'description': '',
               'sunrise': '',
               'sunset': '',
               'title': ''},
       'temperature': {
		       'celsius': '', 
		       'fahrenheit': ''},
       'uvb_index': {
		       'description': '', 
		       'value': },
       'visibility': '',
       'wind': {'direction': 'В',
                'gust': {
		                'km/h': '', 
		                'm/s': '', 
		                'mi/h': ''},
                'speed': {
		                'km/h': '', 
		                'm/s': '', 
		                'mi/h': ''}}},
But sometimes some field may have `No data` in them. In that case that means gismeteo.com didn't show this field, or it was empty.

