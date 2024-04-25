import pygame
import spider

a = spider.get_url()

# 初始化pygame
pygame.init()

# 播放本地mp3文件
mp3_path = r'D:\11.mp3'  # 使用原始字符串来避免转义字符的影响
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()

# 等待音乐播放完毕
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# 停止pygame

pygame.quit()
