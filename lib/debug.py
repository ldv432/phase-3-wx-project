from models.city import City
from models.weather import Weather


City.create_table()
City.create('New York')
City.create('Boston')

import ipdb; ipdb.set_trace() 
# import ipdb
