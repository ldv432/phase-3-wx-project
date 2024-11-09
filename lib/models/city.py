import sqlite3

CONN = sqlite3.connect('lib/weather_data.db')

CURSOR = CONN.cursor

class City:

    all_cities = {}
    def __init__(self, name, region_id, id_=None):
        self.id = id_ #instantiation VS persistence
        self.name = name
        self.region_id = region_id
        type(self).all_cities.append(self)

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS cities (
                           id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           region_id FOREIGN KEY,
                           );
            """) ## DDL Command, doesn't need to be "committed"
        except Exception as e:
            return e
        
    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute("""
                DROP TABLE IF EXISTS cities
        """)
        except Exception as e:
            return e
    
    def save(self):
        try:
            with CONN:
                CURSOR.execute(f"""
                INSERT INTO cities
                (name, region_id)
                VALUES
                (?, ?) 
                """, (self.name, self.region_id)) #line 44/45 "sanitizes" values
                self.id_ = CURSOR.lastrowid
        except Exception as e:
                return e
    
    @classmethod
    def create(cls, name, region_id):
        city = cls(name, region_id)
        city.save()
        return city

    @classmethod

    @property
    def name(self):
        return self._name
        
    @property
    def region_id(self):
        return self._region_id    

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("must be of type string")
        elif not 3 <= len(value) <=50: 
            #  elif not (3<= len(value) <=50):
             raise ValueError("must be between 3 and 50 characters")
        self._name = value
    
    @region_id.setter
    def region_id(self,value):
        if not isinstance(value,int):
            raise ValueError("must be a integer")
        #(find by) elif not region.findby(region_id) (ex we only have 5 regions, but someone looks for region_id 10)
        self._region_id = value
    