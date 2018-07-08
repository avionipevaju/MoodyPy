from moody.moody import Moody
from moody.forecast import Forecast

if __name__ == "__main__":
    moody = Moody()
    weather = Forecast('Belgrade')

    moody.verify_credentials()

    moody.tweet(weather.current_weather() + ' https://www.youtube.com/watch?v=z2elJtgY6h8')
