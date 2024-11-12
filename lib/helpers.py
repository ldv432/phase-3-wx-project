import re

from lib.models.city import City

class Helper:

    #Welcome Message
    @staticmethod
    def welcome():
        print ("Welcome to the Weather History App!")
    

    #Display interactive menu
    @staticmethod
    def menu():
        print("Please select from the options below:")
        print()
        print("1. List all cities")
        print("2. Look up weather history for a city for a certain date")
        print("3. Look up all occurences of a weather event based on type")
        print("4. Look up hottest temperature for a chosen city")
        print("5. Look up the coldest temperature for a chosen city")
        print("6. Look up most humid day for a chosen city")
        print("7. Look up the average high temperature for a chosen city")
        print("8. Look up the average low temperature for a chosen city")

    @staticmethod
    def list_cities():
        if cities := City.get_all():
            for city in cities:
                print(city.name)

    
    @classmethod
    def pascal_to_camel_plural(cls):
        # Use regex to split the class name at capital letters
        words = re.findall('[A-Z][a-z]*', cls.__name__)
        
        # Join the words with underscores
        camel_case_plural = '_'.join(words).lower()
        
        # Pluralize the last word
        if words:
            last_word = words[-1]
            if last_word.endswith('s') or last_word.endswith('x'):
                camel_case_plural += 'es'
            elif last_word.endswith('y'):
                camel_case_plural += 'ies'
            else:
                camel_case_plural += 's'
        
        return camel_case_plural