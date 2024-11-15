import re
import rich
from models.city import City
import ipdb; ipdb.set_trace()
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
        print("2. Exit")
        print()
       

    @staticmethod
    def cities_menu():
        print()

    @staticmethod
    def list_cities():
        if cities := City.get_all():
            print("\nList of Cities:")
            for index, city in enumerate(cities):
                print(f"{index + 1}. {city.name}")
            try:
                city_choice = int(input("Select a city by number to view more weather details, or press 0 to go back: "))
                if city_choice == 0:
                    return
                elif 1 <= city_choice <= len(cities):
                    selected_city = cities[city_choice - 1]
                    Helper.city_details_menu(selected_city)
                else:
                    print("\nInvalid choice, returning to main menu.")
            except ValueError:
                print("\nInvalid input, returning to main menu.")
        else: 
            print("\nNo cities found.")

    @staticmethod
    def city_details_menu(city):
        while True:
            print(f"\nCity Weather Details for {city.name}")
            print("1. View weather by date")
            print("2. View hottest temperature")
            print("3. View coldest temperature")
            print("4. View most humid day")
            print("5. View average high temperature")
            print("6. View average low temperature")
            print("0. Return to city list")
            Helper.city_details_choice(city)
            
    @staticmethod
    def city_details_choice(city):
            try:
                user_choice = (int(input("Select a piece of data to view, or press 0 to go back to cities: ")))
                if user_choice == 1:
                    Helper.weather_by_date(city)
                if user_choice == 2:
                    print(f"{city.hottest_temperature().max_temperature}")
                if user_choice == 3:
                    print(f"{city.coldest_temperature().min_temperature}")
                if user_choice == 4:
                    print(f"{city.most_humid_day().max_humidity}%")
                if user_choice == 5:
                    print(f"{city.average_high_temperature()}")
                if user_choice == 6:
                    print(f"{city.average_low_temperature()}")
                if user_choice == 0:
                    Helper.list_cities()
            except:
                pass

    @staticmethod
    def weather_by_date(city):
        date_choice = (input("Type in a date (Format MM/DD/YYYY): "))
        result = city.weather_history(date_choice)
        if result:
            print(f"\nHere is the weather for {city.name} on {result.forecast_date}:" 
                f"\n\033[31mHigh Temperature: {result.max_temperature}°" " " f"\033[94mLow Temperature: {result.min_temperature}°\033[0m"
                f"\nWeather for the day: {result.weather_conditions}  Humidity: {result.max_humidity}%\033[0m")
        else:
            print("No temperatures exists for this city.")

        

        

