import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill("black")
running = True
x, xer, y, yer = 123, 3, 156, 2
clock = pygame.time.Clock()
r = g = b = 45

def draw(x, y):
    pygame.draw.circle(screen, color, (x, y), 30)

while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    x += xer; y += yer
    if x <= 30 or x >= 770 : xer *= -1
    if y <= 30 or y >= 770 : yer *= -1
    color = (r, g, b)
    r, g, b = random.randint(0, 255), \
    random.randint(0, 255), random.randint(0, 255)
    draw(x, y)
    pygame.display.update()
pygame.quit()
