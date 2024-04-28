import requests
import json
import os
from tqdm import tqdm

api_url = "https://anime-music.jijidown.com/api/v2/music"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.json')
with open(config_path,'r') as file:
    config = json.load(file)

#爬虫
def get_song_data():
    song_data = requests.get(url=api_url,headers=headers)
    song_data = json.loads(song_data.text)
    return song_data

#下载器
def down_url(song_url,song_title):
    path = config['song_path'] + song_title + ".mp3"
    song = requests.get(song_url,stream=True)
    total = int(song.headers.get('content-length', 0))

    with open(path, 'wb') as file, tqdm(
        desc=path+'/'+song_title+'.mp3',
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in song.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


    print('下载完成')
    return path

"""
anime_title  = song_datas['res']['anime_info']['title']
anime_bg_url = song_datas['res']['anime_info']['bg']
anime_desc   = song_datas['res']['anime_info']['desc']
song_title   = song_datas['res']['title']
song_url     = song_datas['res']['play_url']
"""