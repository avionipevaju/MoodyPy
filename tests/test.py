from moody_py.moody import Moody
from moody_py.forecast import Forecast
from moody_py.youtube import YouTube
from moody_py.discogs import Discogs

if __name__ == "__main__":

    moody = Moody()
    moody.verify_credentials()
    weather = Forecast('Belgrade')
    youtube_search_engine = YouTube()
    discogs_search_engine = Discogs().search_engine

    #artist = discogs_search_engine.search('Mogwai', type='artist')[0]
    #print(artist)

    releases = discogs_search_engine.search('Veronautika', type='release')[0]
    #for track in releases.tracklist:
    #    print(track.title)

    track_11 = releases.tracklist[11].title
    print(track_11)

    moody.tweet(weather.current_weather() + ' ' + youtube_search_engine.search_video(track_11))




