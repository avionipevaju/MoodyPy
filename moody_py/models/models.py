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
        if 6 <= hour < 11:
            return TimeOfDay.MORNING
        if 11 <= hour < 17:
            return TimeOfDay.DAY
        if 17 <= hour < 20:
            return TimeOfDay.EVENING
        if 20 <= hour < 24 or 0 < hour < 6:
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


class Instruction:
    """
    Value object representing instruction that the engine should perform
    """

    PROCESS_WEATHER_DATA = "PROCESS_WEATHER_DATA"
    PROCESS_ARTIST = "PROCESS_ARTIST"
    PROCESS_INSTAGRAM_POST = "PROCESS_INSTAGRAM_POST"

    def __init__(self):
        pass


class TwitterPost:
    """
    Data transfer object representing a twitter post
    """

    def __init__(self, post_text, youtube_url, condition, temperature):
        self.post_text = post_text
        self.youtube_url = youtube_url
        self.condition = condition
        self.temperature = temperature


class TwitterResponse:
    """
    Data transfer object representing a twitter response
    """

    _to_string = 'Status {}, Description {}, Post_Id {}, Timestamp {}, Content {}'

    def __init__(self, twitter_status=None, description=None):
        """
        TwitterResponse assembler
        :param twitter_status: twitter.Status object
        """
        if twitter_status is None:
            self.status = -1
            self.description = description
        else:
            self.status = 0
            self.description = 'Successfully posted tweet'
            self.post_id = twitter_status.id
            self.timestamp = twitter_status.created_at
            self.content = twitter_status.text

    def __str__(self):
        return self._to_string.format(self.status, self.description, self.post_id, self.timestamp, self.content)


class ExecutionRequest:
    """
    Data transfer object representing a received request
    """

    def __init__(self, json_request=None):
        """
        ExecutionRequest assembler
        :param json_request: JSON represented execution request
        """
        if json_request is None:
            self.instruction = Instruction.PROCESS_WEATHER_DATA
        else:
            self.instruction = json_request['instruction']
            self.content = json_request['content']
            self.requested_by = json_request['requestedBy']
