from moody.moody import Moody
from moody.forecast import Forecast
from moody.youtube import YouTube

if __name__ == "__main__":
    moody = Moody()
    weather = Forecast('Belgrade')

    moody.verify_credentials()

    video = YouTube()
    print(video.search_video('Mogwai'))

    #moody.tweet(weather.current_weather() + ' https://www.youtube.com/watch?v=z2elJtgY6h8')


