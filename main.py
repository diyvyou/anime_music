import pygame
import spider

song_data_list = {'msg':0}

#解析器
def get_song():
    song_data = spider.get_song_data()
    song_title   = song_data['res']['title']
    song_url     = song_data['res']['play_url']
    anime_title  = song_data['res']['anime_info']['title']
    #print(song_data)
    return song_title,song_url,anime_title

#播放器
def play_song(song_path,song_title,anime_title):
    pygame.init()
    print('动漫：' + anime_title)
    print('正在播放：' + song_title)
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()



def main():
    title,url,anime_title = get_song()
    path = spider.down_url(url,title)
    play_song(path,title,anime_title)

main()
