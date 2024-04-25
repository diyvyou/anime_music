import requests
import json

api_url = "https://anime-music.jijidown.com/api/v2/music"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}


song_datas = requests.get(url=api_url,headers=headers)
song_datas = json.loads(song_datas.text)


anime_title  = song_datas['res']['anime_info']['title']
anime_bg_url = song_datas['res']['anime_info']['bg']
anime_desc   = song_datas['res']['anime_info']['desc']
song_title   = song_datas['res']['title']
song_url     = song_datas['res']['play_url']

print(song_url)