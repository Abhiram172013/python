import pygame,random
pygame.init()
w,h=800,600
s=pygame.display.set_mode((w,h))
p=pygame.Rect(400,300,40,40)
en=[pygame.Rect(random.randint(0,w-40),random.randint(0,h-40),40,40) for _ in range(7)]
score=0
c=pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); exit()
    k=pygame.key.get_pressed()
    p.x+=5*(k[pygame.K_RIGHT]-k[pygame.K_LEFT])
    p.y+=5*(k[pygame.K_DOWN]-k[pygame.K_UP])
    for i in en:
        if p.colliderect(i):
            score+=1
            i.x,i.y=random.randint(0,w-40),random.randint(0,h-40)
    s.fill((0,0,0))
    pygame.draw.rect(s,(0,255,0),p)
    [pygame.draw.rect(s,(255,0,0),i) for i in en]
    pygame.display.set_caption(str(score))
    pygame.display.update()
    c.tick(60)