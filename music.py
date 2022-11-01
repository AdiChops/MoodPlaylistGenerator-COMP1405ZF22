import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

start = time.time()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sad_results = spotify.playlist_tracks("spotify:playlist:6nxPNnmSE0d5WlplUsa5L3")

fileout = open("song_features.txt", "w")
min_loudness = None
max_loudness = None
results = []

for track in sad_results['items']:
    feature = spotify.audio_features(track['track']['uri'])
    results.append([feature[0]["valence"], feature[0]["danceability"], feature[0]["energy"], feature[0]["loudness"], 0])

happy_results = spotify.playlist_tracks("spotify:playlist:0RH319xCjeU8VyTSqCF6M4")
for track in happy_results['items']:
    feature = spotify.audio_features(track['track']['uri'])
    results.append([feature[0]["valence"], feature[0]["danceability"], feature[0]["energy"], feature[0]["loudness"], 1])

chill_results = spotify.playlist_tracks("spotify:playlist:0yP9zFyPa0mal4fTRo2Ey9")
for track in chill_results['items']:
    feature = spotify.audio_features(track['track']['uri'])
    results.append([feature[0]["valence"], feature[0]["danceability"], feature[0]["energy"], feature[0]["loudness"], 2])

for result in results:
    if min_loudness is None or result[3] < min_loudness:
        min_loudness = result[3]
    if max_loudness is None or result[3] > max_loudness:
        max_loudness = result[3]

fileout = open("song_features.txt", "w")
for result in results:
    result[3] = (result[3] - min_loudness) / (max_loudness - min_loudness)
    fileout.write(f"{result[0]},{result[1]},{result[2]},{result[3]},{result[4]}\n")
end = time.time()
print("It took " + str(end - start) + " ms to run this program.")