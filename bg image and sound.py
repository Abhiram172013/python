import pygame

pygame.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1)

s=pygame.display.set_mode((600,400))
bg=pygame.image.load("bg.jpg")

while True:
    s.blit(bg,(0,0))
    pygame.display.update()