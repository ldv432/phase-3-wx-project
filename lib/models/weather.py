from datetime import datetime
from models.city import City
import ipdb
from models.__init__ import CURSOR, CONN

class Weather:
    def __init__(self, city_id, forecast_date, weather_conditions, max_temperature, min_temperature, max_wind, max_humidity, id=None):
        self.id = id,
        self.city_id = city_id # city_id is foreign key
        self.forecast_date = forecast_date 
        self.weather_conditions = weather_conditions
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.max_wind = max_wind
        self.max_humidity = max_humidity

    
    
    @property
    def city_id(self):
        return self._city_id
    
    @city_id.setter
    def city_id(self, city_id):
        if not isinstance(city_id, int):
            raise TypeError("City_id must be an integer")
        elif city_id < 1 or not City.find_by_id(city_id):
            raise ValueError(
                "City ID must be a positive integer and pointing to an existing city"
            )
        else:
            self._city_id = city_id

    
    @property
    def forecast_date(self):
        return self._forecast_date
    
    @forecast_date.setter
    def forecast_date(self, forecast_date):
        if not isinstance(forecast_date, str):
            raise TypeError("Date entered must be a string with format MM/DD/YYYY")
        elif datetime.strptime(forecast_date, '%m/%d/%Y'):
            raise ValueError("Date must be in the format MM/DD/YYYY")
        self._forecast_date = forecast_date

    @property
    def weather_conditions(self):
        return self._weather_conditions
    
    @weather_conditions.setter
    def weather_conditions(self, weather_conditions):
        if not isinstance(weather_conditions, str):
            raise TypeError("Input must be a string")
        self._weather_conditions = weather_conditions


    @property
    def max_temperature(self):
        return self._max_temperature
    
    @max_temperature.setter
    
    @property
    def min_temperature(self):
        return self._min_temperature
    
    @property
    def max_wind(self):
        return self._max_wind
    
    @property
    def max_humidity(self):
        return self._max_humidity
    
    ### WEATHER CLASS ORM METHODS ###

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS weathers (
                           id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL
                           ); 
            """)
            # region_id INTEGER 
            # FOREIGN KEY (region_id) REFERENCES regions(id),
            ## DDL Command, doesn't need to be "committed"
        except Exception as e:
            return e
        
    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute("""
                DROP TABLE IF EXISTS weathers
        """)
        except Exception as e:
            return e
    
    
    @classmethod
    def new_from_db(cls, row):
        return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
    
    @classmethod
    def get_all(cls):
        try:
            with CONN:
                query = CURSOR.execute(f"""
                    SELECT * FROM weathers
                """)
                data = query.fetchall()
                return [cls.new_from_db(row) for row in data]
        except Exception as e:
            return e
        
    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                query = CURSOR.execute(f"""
                SELECT * FROM weathers
                WHERE name=?
                LIMIT 1;
                """, (name.lower(),))
                row_of_data = query.fetchone()
                return cls.new_from_db(row_of_data) if row_of_data else None
        except Exception as e:
            return e
        
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("""
                    SELECT * FROM weathers
                    WHERE id is ?;
                    """, (id,)
                    )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0]) if row else None
            
        ###  ORM Instance Methods  ###

    # def save(self):
    #     try:
    #         with CONN:
    #             CURSOR.execute(f"""
    #             INSERT INTO weathers
    #             (name)
    #             VALUES
    #             (?) 
    #             """, (self.name,)) #line 44/45 "sanitizes" values
    #             self.id_ = CURSOR.lastrowid
    #     except Exception as e:
    #             return e
    

    # def delete(self):
    #     try:
    #         with CONN:
    #             CURSOR.execute(f"""
    #             DELETE FROM weathers
    #             WHERE id = ?;
    #             """, (self.id,))
    #             del type(self).all_[self.id]
    #     except Exception as e:
    #         return e

        #### ASSOCIATION METHOD ####

    def city(self):
        return City.find_by_id(self.city_id) if self.city_id else None