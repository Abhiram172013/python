import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 50, 50)
box = pygame.Rect(350, 200, 50, 50)
speed = 5
run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]: player.x -= speed
    if k[pygame.K_RIGHT]: player.x += speed
    if k[pygame.K_UP]: player.y -= speed
    if k[pygame.K_DOWN]: player.y += speed

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),player)
    pygame.draw.rect(screen,(255,0,0),box)
    pygame.display.update()
    clock.tick(60)

pygame.quit()