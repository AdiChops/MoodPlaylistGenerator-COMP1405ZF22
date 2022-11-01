import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.audio_features('spotify:track:4ly1bQiQoFw5FgY49QccGg')
# print(results)

auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)


token = util.prompt_for_user_token("<username>",'user-modify-public',client_id=os.getenv("SPOTIPY_CLIENT_ID"),client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),redirect_uri='http://localhost:8080/callback') 
sp = spotipy.Spotify(auth=token)

playlist_name = f"Playlist Mood Test"
list_of_tracks = ["spotify:track:4ly1bQiQoFw5FgY49QccGg", 'spotify:track:3S68RFe1lsdCdTMPIMJM3X']

def GetPlaylistID(username, playlist_name):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:  # iterate through playlists I follow
        if playlist['name'] == playlist_name:  # filter for newly created playlist
            return playlist['id']
    return None

sp.user_playlist_create("<username>", name=playlist_name)

sp.playlist_add_items(GetPlaylistID("<username>", "Playlist Mood Test"), list_of_tracks)

# Order to determine mood
# ORDER:
# 1. valence
# 2. danceability
# 3. energy
# 4. loudness

# def determineSongMood(song):
#     result = spotify.audio_features(song)
#     valence = result[0]['valence'] * 100
#     danceability = result[0]['danceability'] * 50
#     energy = result[0]['energy'] * 25
#     loudness = result[0]['loudness']

