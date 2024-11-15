from models.__init__ import CURSOR, CONN

# from models.weather import Weather

# from helpers import Helper


class City:

    all_cities = {}

    def __init__(self, name, id_=None):
        self.id = id_  # instantiation VS persistence
        self.name = name
        # type(self).all_cities.append(self)

        ###  ORM Class Methods  ###

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS cities (
                           id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL
                           ); 
            """
            )
            # region_id INTEGER
            # FOREIGN KEY (region_id) REFERENCES regions(id),
            ## DDL Command, doesn't need to be "committed"
        except Exception as e:
            return e

    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(
                """
                DROP TABLE IF EXISTS cities
        """
            )
        except Exception as e:
            return e

    @classmethod
    def create(cls, name):
        city = cls(name)
        city.save()
        return city

    @classmethod
    def new_from_db(cls, row):
        return cls(row[1], row[0])

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                query = CURSOR.execute(
                    f"""
                    SELECT * FROM cities
                """
                )
                data = query.fetchall()
                return [cls.new_from_db(row) for row in data]
        except Exception as e:
            return e

    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                query = CURSOR.execute(
                    f"""
                SELECT * FROM cities
                WHERE name=?
                LIMIT 1;
                """,
                    (name.lower(),),
                )
                row_of_data = query.fetchone()
                return cls.new_from_db(row_of_data) if row_of_data else None
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
                    SELECT * FROM cities
                    WHERE id is ?;
                    """,
            (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

        ###  ORM Instance Methods  ###

    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                INSERT INTO cities
                (name)
                VALUES
                (?) 
                """,
                    (self.name,),
                ) 
                self.id = CURSOR.lastrowid
        except Exception as e:
            return e

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                DELETE FROM cities
                WHERE id = ?;
                """,
                    (self.id,),
                )
                del type(self).all_[self.id]
        except Exception as e:
            return e

        ###  PROPERTIES  ###

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("must be of type string")
        elif not 3 <= len(value) <= 50:
            raise ValueError("must be between 3 and 50 characters")
        self._name = value

    ### ASSOCIATION METHODS ###
    def weathers(self):
        CURSOR.execute(
            """
                SELECT * FROM weathers
                WHERE city_id = ?
                """,
            (self.id,),
        )
        rows = CURSOR.fetchall()
        return [
            Weather(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
            for row in rows
        ]

    def weather_history(self, date):
        try:
            for weather in self.weathers():
                if weather.forecast_date == date:
                    return weather
            return "Weather for this date could not be found."
        except Exception as e:
            return f"An error occurred while retrieving weather history: {e}"

    def hottest_temperature(self):
        print(f"\nShowing hottest temperature for {self.name}")
        return max(
            self.weathers(), key=lambda weather: weather.max_temperature, default=None
        )

    def coldest_temperature(self):
        print(f"\nShowing coldest temperature for {self.name}")
        return min(
            self.weathers(), key=lambda weather: weather.min_temperature, default=None
        )

    def most_humid_day(self):
        print(f"\nShowing most humid day for {self.name}")
        return max(
            self.weathers(), key=lambda weather: weather.max_humidity, default=None
        )

    def average_high_temperature(self):
        print(f"Showing average high temperature for {self.name}")
        temp_list = [self.max_temperature for self in self.weathers()]
        return sum(temp_list) / len(temp_list)

    # add all the max temperatures... len(max_temperature) => how many numbers are in the collection
    # add all the max temperatures and then divide by that number of how many max temps there are

    def average_low_temperature(self):
        print(f"Showing average low temperature for {self.name}")
        temp_list = [self.min_temperature for self in self.weathers()]
        return sum(temp_list) / len(temp_list)


from models.weather import Weather
