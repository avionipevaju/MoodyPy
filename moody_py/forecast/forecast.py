from weather import Weather, Unit
import logging


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
        weather = Weather(unit=unit)
        self.location = weather.lookup_by_location(city)

    def current_weather(self):
        """
        Gets the current weather for a city
        :return: Current weather
        """
        condition = self.location.condition
        return (self.location.description + ', Temperature: ' + condition.temp + 'C' + ', Time: ' + condition.date
                + ', Condition: ' + condition.text)
