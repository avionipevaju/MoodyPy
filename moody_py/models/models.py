import datetime


class WeatherData:
    """
    Data transfer object containing relevant weather data
    """

    _to_string = 'Location: {}, Condition: {}, Condition Code: {}, Temperature: {}, Date: {}, Time: {}, {}'

    def __init__(self, weather_object):
        """
        Weather data assembler
        :param weather_object: Yahoo Weather weather_object
        """
        self.location = self.resolve_location(weather_object.description)
        self.condition = weather_object.condition.text
        self.condition_code = weather_object.condition.code
        self.temperature = weather_object.condition.temp
        self.date = weather_object.condition.date
        self.time = datetime.datetime.time(datetime.datetime.now())
        self.time_of_day = self.get_time_of_day()

    @staticmethod
    def resolve_location(yahoo_description):
        """
        Extracts the location from Yahoo weather description
        :param yahoo_description: Yahoo weather description
        :return: Location name
        """
        return yahoo_description.split(" ")[4][:-1]

    def get_time_of_day(self):
        hour = self.time.hour
        if 6 < hour < 11:
            return TimeOfDay.MORNING
        if 11 < hour < 17:
            return TimeOfDay.DAY
        if 17 < hour < 20:
            return TimeOfDay.EVENING
        if 20 < hour < 24 or 0 < hour < 6:
            return TimeOfDay.NIGHT

    def __str__(self):
        return self._to_string.format(self.location, self.condition, self.condition_code, self.temperature, self.date,
                                      self.time, self.time_of_day)


class TimeOfDay:
    """
    Value object representing time of day
    """

    MORNING = "Morning"
    DAY = "Day"
    EVENING = "Evening"
    NIGHT = "Night"

    def __init__(self):
        pass


class PostContent:
    """
    Data transfer object representing relevant post content
    """

    def __init__(self, genre, text):
        self.genre = genre
        self.text = text
