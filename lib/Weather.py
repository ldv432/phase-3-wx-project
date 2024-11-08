from datetime import datetime
import ipdb
class Weather:
    def __init__(self, id, city_id, forecast_date, weather_conditions, max_temperature, min_temperature, max_wind, max_humidity):
        self.id = id,
        self.city_id = city_id # city_id is foreign key
        self.forecast_date = forecast_date 
        self.weather_conditions = weather_conditions
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.max_wind = max_wind
        self.max_humidity = max_humidity
        pass

    @property
    def id(self):
        return self._id
    
    @property
    def city_id(self):
        return self._city_id
    
    @property
    def forecast_date(self):
        return self._forecast_date
    
    @forecast_date.setter
    def forecast_date(self, forecast_date):
        if not isinstance(forecast_date, str):
            raise TypeError("Date entered must be a string with format MM/DD/YY")
        elif datetime.strptime(forecast_date, '%m/%d/%Y'):
            raise ValueError("Date must be in the format MM/DD/YYYY")
        self._forecast_date = forecast_date

    @property
    def weather_conditions(self):
        return self._weather_conditions

    @property
    def max_temperature(self):
        return self._max_temperature
    
    @property
    def min_temperature(self):
        return self._min_temperature
    
    @property
    def max_wind(self):
        return self._max_wind
    
    @property
    def max_humidity(self):
        return self._max_humidity

instance = Weather("11/05/2024")
ipdb.set_trace()
instance.forecast_date