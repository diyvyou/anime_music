import pygame
import spider


song_datas = spider.get_song()
song_datalist = spider.get_song_datas(song_datas)

# 获取信息
song_title = song_datalist['song_title']
song_url = song_datalist['song_url']
song_path = spider.down_url(song_url,song_title) # 使用原始字符串来避免转义字符的影响

#播放器
def play_song(song_path):
    pygame.init()
    print('正在播放：' + song_title)
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()

play_song(song_path)