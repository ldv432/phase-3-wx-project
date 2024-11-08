class Weather:
    def __init__(self, id, city_id, forecast_date, weather_conditions,max_temperature, min_temperature,  humidity):
        self.id = id, 
        # city_id is foregin key
        self.city_id = city_id 
        self.forecast_date = forecast_date 
        self.weather_conditions = weather_conditions
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        # self.realwind = realwind
        self.humidity = humidity
        pass