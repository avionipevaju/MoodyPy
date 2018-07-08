from weather import Weather, Unit
import logging


class Forecast:
    """
    Provides weather information for a given location by using Yahoo Weather API.
    """

    def __init__(self, city, unit=Unit.CELSIUS):
        logging.info('Configuring weather data for %s in %s', city, unit)
        weather = Weather(unit=unit)
        self.location = weather.lookup_by_location(city)

    def current_weather(self):
        condition = self.location.condition
        return (self.location.description + ', Temperature: ' + condition.temp + 'C' + ', Time: ' + condition.date
                + ', Condition: ' + condition.text)



