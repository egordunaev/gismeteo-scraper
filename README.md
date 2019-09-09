# GisMeteoScraper

This is a python web scraper for [gismeteo](https://www.gismeteo.com/), it scrapes all html content from webpage.


### Requirements

GisMeteoScraper uses libraries such as:
* requests
* bs4 (BeautifulSoup4)

GisMeteoScraper is also built on `python 3.7.3`

### Usage example

    from scraper import GisMeteoScraper
    
    gis = GisMeteoScraper("link to gismeteo with town")
    weather = gis.scrape_info()


### Output
GisMeteoScraper's `scrape_info()` outputs `dict()` object, which contains weather on each timeslot `as int()` *(like 0, or 21)*, for example:

    timeslot: 
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
       'wind': {'direction': '',
                'gust': {
		                'km/h': '', 
		                'm/s': '', 
		                'mi/h': ''},
                'speed': {
		                'km/h': '', 
		                'm/s': '', 
		                'mi/h': ''}}},

Note:
> Description values *like `humidity[description]`* may contain text according to your region.
> For example `SW` (South-West) in English -> `ЮВ` (Юго-Восток) in Russian, and so on.

But sometimes some field may have `No data` in them. That's probably because [gismeteo](https://www.gismeteo.com/) didn't show this field, or it was empty. Also, returning `dict()` may contain `_error` field if there was any.

If you have any questions or issues, you can see all issues [here](https://github.com/egordunaev/gismeteo-scraper/issues), alternatively you can [create a new issue](https://github.com/egordunaev/gismeteo-scraper/issues/new)
