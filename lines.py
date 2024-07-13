import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill("black")
running = True
clock = pygame.time.Clock()
lines = [(0, 0), (0, 800), (800, 0), (800, 800),(400,400),
         (0, 400), (400, 0), (800, 400), (400, 800)]

def draw():
    for line in range(len(lines)):
        pygame.draw.line(screen, "white", lines[line],
                          pygame.mouse.get_pos())
        pygame.draw.line(screen, "white", lines[line], (400, 400), 1)

while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    r, g, b = random.randint(0, 255), \
    random.randint(0, 255), random.randint(0, 255)
    screen.fill("black")
    if pygame.mouse.get_pos() != (0, 0):draw()

    pygame.display.update()
pygame.quit()