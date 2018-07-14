from moody_py import utils


class WeatherData:
    """
    Value object containing relevant weather data
    """
    _to_string = 'Location: {}, Condition: {}, Condition Code: {}, Temperature: {}, Date: {}'

    def __init__(self, weather_object):
        """
        Weather data assembler
        :param weather_object: Yahoo Weather weather_object
        """
        self.location = utils.resolve_location(weather_object.description)
        self.condition = weather_object.condition.text
        self.condition_code = weather_object.condition.code
        self.temperature = weather_object.condition.temp
        self.date = weather_object.condition.date

    def __str__(self):
        return self._to_string.format(self.location, self.condition, self.condition_code, self.temperature, self.date)
