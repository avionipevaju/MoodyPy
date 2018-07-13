from moody_py.engine.moody import Moody
from moody_py.forecast.forecast import Forecast
from moody_py.youtube.youtube import YouTube
from moody_py.discogs.discogs import Discogs

if __name__ == "__main__":

    moody = Moody()
    moody.verify_credentials()
    weather = Forecast('Belgrade')
    youtube_search_engine = YouTube()
    discogs = Discogs()

    artist = 'Mogwai'
    track = discogs.get_random_track_by_artist(artist)
    print(track)

    track_by_genre = discogs.get_random_track_by_genre('Post+Rock')
    print(track_by_genre)

    moody.tweet(weather.current_weather() + ' ' + youtube_search_engine.search_video(track_by_genre))





