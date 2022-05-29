from bs4 import BeautifulSoup
from urllib.request import urlretrieve
urlretrieve('https://www.openstreetmap.org/api/0.6/map?bbox=37.5649%2C55.5586%2C37.5803%2C55.5728', 'map.osm')
xml = open('map.osm', 'r', encoding='utf-8').read()
# <bounds minlat="55.5586000" minlon="37.5649000" maxlat="55.5728000" maxlon="37.5803000"/>
