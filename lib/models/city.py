import sqlite3

CONN = sqlite3.connect('lib/weather_data.db')

CURSOR = CONN.cursor()

# from helpers import Helper

class City:

    all_cities = {}

    def __init__(self, name, id_=None):
        self.id = id_ #instantiation VS persistence
        self.name = name
        # type(self).all_cities.append(self)

            ###  ORM Class Methods  ###

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS cities (
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
                DROP TABLE IF EXISTS cities
        """)
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
                query = CURSOR.execute(f"""
                    SELECT * FROM cities
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
                SELECT * FROM cities
                WHERE name=?
                LIMIT 1;
                """, (name.lower(),))
                row_of_data = query.fetchone()
                return cls.new_from_db(row_of_data) if row_of_data else None
        except Exception as e:
            return e
            
        ###  ORM Class Methods  ###

    def save(self):
        try:
            with CONN:
                CURSOR.execute(f"""
                INSERT INTO cities
                (name)
                VALUES
                (?) 
                """, (self.name,)) #line 44/45 "sanitizes" values
                self.id_ = CURSOR.lastrowid
        except Exception as e:
                return e
    

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(f"""
                DELETE FROM cities
                WHERE id = ?;
                """, (self.id,))
                del type(self).all_[self.id]
        except Exception as e:
            return e
        
        ###  PROPERTIES  ###

    @property
    def name(self):
        return self._name
          

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("must be of type string")
        elif not 3 <= len(value) <=50: 
            #  elif not (3<= len(value) <=50):
             raise ValueError("must be between 3 and 50 characters")
        self._name = value
    
    
    