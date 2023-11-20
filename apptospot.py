import spotipy, xmltodict
from spotipy.oauth2 import SpotifyOAuth

# Spotify APIの認証情報
SPOTIPY_CLIENT_ID = "your client id"
SPOTIPY_CLIENT_SECRET = "your client secret"
SPOTIPY_REDIRECT_URI = "your redirect uri"  # I used http://localhost:8888/callback
SPOTIPY_USERNAME = "your username"

# Spotify APIにアクセス
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        SPOTIPY_CLIENT_ID,
        SPOTIPY_CLIENT_SECRET,
        SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-public playlist-modify-private",
        username=SPOTIPY_USERNAME,
    )
)
# XMLデータを読み込む
with open("ミュージック.xml", "r", encoding="utf-8") as file:
    music_data = xmltodict.parse(file.read())

# プレイリストの作成
playlist_name = "FromSpotipy"
playlist_description = "Playlist created from Music.xml"
playlist = sp.user_playlist_create(
    sp.me()["id"], playlist_name, public=False, description=playlist_description
)

# 各楽曲に対してSpotifyで検索してプレイリストに追加
i = 0
todolist = []
for track_id, track_info in music_data["dict"].items():
    if i == 0:
        i += 1
        continue
    for track in track_info:
        track_name = track["string"][0]
        artist_name = track["string"][1]

        # Spotifyで曲を検索
        results = sp.search(q=f"{track_name} {artist_name}", type="track", limit=1)

        # 検索結果があればプレイリストに追加
        if results["tracks"]["items"]:
            track_uri = results["tracks"]["items"][0]["uri"]
            sp.playlist_add_items(playlist["id"], [track_uri])
            print(f"Added {track_name} by {artist_name} to the playlist.")
        else:
            print(f"Could not find {track_name} by {artist_name} on Spotify.")
            todolist.append(f"{track_name} by {artist_name}")
print(todolist)
