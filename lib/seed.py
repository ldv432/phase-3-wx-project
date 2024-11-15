from models.city import City
from models.weather import Weather

from random import sample
from faker import Faker
fake = Faker()

Weather.drop_table()
City.drop_table()
Weather.create_table()
City.create_table()


city1 = City.create("New York")
city2 = City.create("Los Angeles")
city3 = City.create("Chicago")
city4 = City.create("Houston")
city5 = City.create("Phoenix")

weather1 = Weather.create(
    city_id=1,
    forecast_date="11/18/2024",
    weather_conditions="sunny",
    max_temperature=78,
    min_temperature=65,
    max_humidity=80
)

weather2 = Weather.create(
    city_id=1,
    forecast_date="11/18/2024",
    weather_conditions="rainy",
    max_temperature=75,
    min_temperature=60,
    max_humidity=85
)

weather3 = Weather.create(
    city_id=2,
    forecast_date="11/18/2024",
    weather_conditions="cloudy",
    max_temperature=70,
    min_temperature=55,
    max_humidity=90
)

weather4 = Weather.create(
    city_id=2,
    forecast_date="11/18/2024",
    weather_conditions="stormy",
    max_temperature=68,
    min_temperature=50,
    max_humidity=95
)

weather5 = Weather.create(
    city_id=3,
    forecast_date="11/18/2024",
    weather_conditions="clear",
    max_temperature=80,
    min_temperature=62,
    max_humidity=70
)

weather6 = Weather.create(
    city_id=1,
    forecast_date="11/19/2024",
    weather_conditions="partly cloudy",
    max_temperature=72,
    min_temperature=58,
    max_humidity=78
)

weather7 = Weather.create(
    city_id=1,
    forecast_date="11/20/2024",
    weather_conditions="sunny",
    max_temperature=76,
    min_temperature=60,
    max_humidity=65
)

# Additional weather entries for Los Angeles
weather8 = Weather.create(
    city_id=2,
    forecast_date="11/19/2024",
    weather_conditions="sunny",
    max_temperature=77,
    min_temperature=63,
    max_humidity=60
)

weather9 = Weather.create(
    city_id=2,
    forecast_date="11/20/2024",
    weather_conditions="foggy",
    max_temperature=70,
    min_temperature=58,
    max_humidity=85
)

# Additional weather entries for Chicago
weather10 = Weather.create(
    city_id=3,
    forecast_date="11/19/2024",
    weather_conditions="windy",
    max_temperature=68,
    min_temperature=52,
    max_humidity=75
)

weather11 = Weather.create(
    city_id=3,
    forecast_date="11/20/2024",
    weather_conditions="rainy",
    max_temperature=65,
    min_temperature=50,
    max_humidity=88
)

# Additional weather entries for Houston
weather12 = Weather.create(
    city_id=4,
    forecast_date="11/18/2024",
    weather_conditions="humid",
    max_temperature=85,
    min_temperature=70,
    max_humidity=90
)

weather13 = Weather.create(
    city_id=4,
    forecast_date="11/19/2024",
    weather_conditions="sunny",
    max_temperature=88,
    min_temperature=72,
    max_humidity=80
)

weather14 = Weather.create(
    city_id=4,
    forecast_date="11/20/2024",
    weather_conditions="rainy",
    max_temperature=82,
    min_temperature=68,
    max_humidity=85
)

# Additional weather entries for Phoenix
weather15 = Weather.create(
    city_id=5,
    forecast_date="11/19/2024",
    weather_conditions="hot",
    max_temperature=90,
    min_temperature=75,
    max_humidity=40
)

weather16 = Weather.create(
    city_id=5,
    forecast_date="11/20/2024",
    weather_conditions="clear",
    max_temperature=88,
    min_temperature=73,
    max_humidity=42
)
