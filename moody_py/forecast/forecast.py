import logging

from weather import Weather, Unit

from moody_py.models.models import WeatherData


class Forecast:
    """
    Provides weather information for a given location by using Yahoo Weather API.
    """
    def __init__(self, city, unit=Unit.CELSIUS):
        """
        Initializes the Forecast engine with settings for a given city and temperature unit
        :param city: City of interest
        :param unit: Temperature unit
        """
        logging.info('Configuring weather data for %s in %s', city, unit)
        self.weather = Weather(unit=unit)
        self.city = city

    def current_weather(self):
        """
        Gets the current weather for a city
        :return: Weather Data representing the current weather of a city
        """
        return WeatherData(self.weather.lookup_by_location(self.city))
