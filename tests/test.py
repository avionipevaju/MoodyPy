from moody_py.moody import Moody
from moody_py.forecast import Forecast
from moody_py.youtube import YouTube
from moody_py.discogs import Discogs

if __name__ == "__main__":

    moody = Moody()
    moody.verify_credentials()
    weather = Forecast('Belgrade')
    youtube_search_engine = YouTube()
    discogs = Discogs()

    artist = 'Chroma Key'
    track = discogs.get_random_track_by_artist(artist)

    search_criteria = artist + ' ' + track
    print(search_criteria)

    moody.tweet(weather.current_weather() + ' ' + youtube_search_engine.search_video(search_criteria))




