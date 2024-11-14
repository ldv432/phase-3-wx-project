import re

from models.city import City

class Helper:

    #Welcome Message
    @staticmethod
    def welcome():
        print ("Welcome to the Last Week of Weather App")
    

    #Display interactive menu
    @staticmethod
    def menu():
        print("Please select from the options below:")
        print("\n1. List all cities")
        # print("2. Look up weather history ")
        # print("3. Look up all occurences of a weather event based on type")
        # print("4. Look up hottest temperature for a chosen city")
        # print("5. Look up the coldest temperature for a chosen city")
        # print("6. Look up most humid day for a chosen city")
        # print("7. Look up the average high temperature for a chosen city")
        # print("8. Look up the average low temperature for a chosen city")

    @staticmethod
    def cities_menu():
        print()

    @staticmethod
    def list_cities():
        if cities := City.get_all():
            print("\nList of Cities:")
            for index, city in enumerate(cities):
                print(f"{index}. {city.name}")
            
            try:
                city_choice = int(input("Select a city by number to view more weather details, or press 0 to go back"))
                if city_choice == 0:
                    return
                elif 1 <= city_choice <= len(cities):
                    selected_city = cities[city_choice - 1]
                    Helper.city_details_menu(selected_city)
                else:
                    print("Invalid choice, returning to main menu.")
            except ValueError:
                print("Invalid input, returning to main menu.")
        else: 
            print("No cities found.")

    @staticmethod
    def city_details_menu(city):
        while True:
            print(f"\nCity Details for {city.name} in the last 7 days:")
            print("1. View the daily weather")
            print("2. View hottest temperature")
            print("3. View coldest temperature")
            print("4. View most humid day")
            print("5. View average high temperature")
            print("6. View average low temperature")
            print("0. Return to city list")



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
    


    # def menu():
    #     print("Please select from the options below:")
    #     print()
    #     print("1. Last Week Of Weather For A City")
            # 1) New York
            #       #past week of weather
            # 2) Boston
            #       #past week of weather
    ###   Don't NEED this == print("2. Look up weather history ") 
    #     print("3. Look up all occurences of a weather event based on type")
        # 3 => 
        #     1) Tornado
        #         [New York 1-6-2023]
        #     2) Blizzard
        #     3) Snow
        #     4) Go back to previous menu
    #     print("4. Look up hottest temperature for a chosen city")
        # 4 => 
        #     1) New York
        #         max([create list of all new york maxtemp])
        #     2) Boston
        #     3) Go back to previous menu
    #     print("5. Look up the coldest temperature for a chosen city")
        # 5 => 
        #     1) New York
        #         min([create list of all new york maxtemp])
        #     2) Boston
        #     3) Go back to previous menu
    #     print("6. Look up most humid day for a chosen city")
        # 6 => 
        #     1) New York
        #         max([create list of all new york humidity])
        #     2) Boston
        #     3) Go back to previous menu
    #     print("7. Look up the average high temperature for a chosen city")
        # 7 => 
            #     1) New York
            #         max([create list of all new york humidity])
            #     2) Boston
            #     3) Go back to previous menu
    #     print("8. Look up the average low temperature for a chosen city")
