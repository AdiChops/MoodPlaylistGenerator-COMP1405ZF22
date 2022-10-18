import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:track:3S68RFe1lsdCdTMPIMJM3X'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.audio_features(lz_uri)

print(results)