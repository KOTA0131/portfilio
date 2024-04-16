import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id="84b88dd9095c4f88a216946cff32a14c",
        client_secret="2ba63e6fb3e94ea4814262375b4f538b",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="晃大"
    )
)
user_id = sp.current_user()["id"]

