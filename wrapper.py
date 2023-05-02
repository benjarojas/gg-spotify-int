import spotipy
from spotipy.oauth2 import SpotifyOAuth

clientid=""
clientsecret=""
redirecturi="http://localhost:8080"
scope="user-read-currently-playing user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid, client_secret=clientsecret, redirect_uri=redirecturi, scope=scope))

def get_current_song():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['item']['name']
    
def get_current_artist():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['item']['artists'][0]['name']
    
def get_current_album():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['item']['album']['name']
    
def get_current_artwork():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['item']['album']['images'][0]['url']
    
def get_current_progress():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['progress_ms']

def get_current_duration():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['item']['duration_ms']
    
def get_current_progress_percent():
    current_song = sp.current_user_playing_track()
    if current_song is None:
        return None
    else:
        return current_song['progress_ms']/current_song['item']['duration_ms']
    
def seconds_to_minutes_and_seconds(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return str(minutes) + ":" + str(seconds).zfill(2)
    
def next_song():
    sp.next_track()

def previous_song():
    sp.previous_track()