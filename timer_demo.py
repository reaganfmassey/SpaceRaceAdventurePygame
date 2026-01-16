import pygame

pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Solar System Sandbox")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 25))   # draw: background
    pygame.display.flip()       # show what we drew
    clock.tick(60)              # 60 frames per second

pygame.quit()