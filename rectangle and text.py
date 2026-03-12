import pygame
pygame.init()

screen = pygame.display.set_mode((600,400))
font = pygame.font.Font(None,40)
text = font.render("Hello",True,(255,255,255))

running = True
while running:
    for event in pygame.event.get():
        if event in pygame == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),(250,150,100,50))
    screen.blit(text,(260,100))
    pygame.display.update()

pygame.quit()