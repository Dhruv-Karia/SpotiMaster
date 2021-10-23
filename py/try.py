import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="f4c17d1f14ea4bfa8ef898a4a2f39706",
                                               client_secret="cfa6d9a1321c4a61a01643ddc96c7cf5",
                                               redirect_uri="http://localhost:1410/",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])