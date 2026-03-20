import pygame
pygame.init()
s=pygame.display.set_mode((300,200))
a=pygame.Surface((40,40));b=pygame.Surface((40,40))
c=(255,0,0);a.fill(c);b.fill(c)
e=pygame.USEREVENT+1;pygame.time.set_timer(e,800)
r=1
while r:
 for i in pygame.event.get():
  if i.type==pygame.QUIT:r=0
  if i.type==e:
   c=(0,255,0)if c==(255,0,0)else(255,0,0)
   a.fill(c);b.fill(c)
 s.fill((0,0,0))
 s.blit(a,(80,80));s.blit(b,(130,80))
 pygame.display.flip()
pygame.quit()