from models.city import City
from models.weather import Weather
import ipdb

City.create_table()
City.create('New York')
City.create('Boston')
