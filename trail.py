import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill("black")
running = True
clock = pygame.time.Clock()
now = prev = (0, 0)
color = ["red", "orange", "green", "red", "white"]

def draw(prev, now):
    for line in range(-10 , 10, 5):
        pygame.draw.line(screen, color[(line + 10) // 5], (prev[0]-line, prev[1]-line), 
                         (now[0]-line, now[1]-line), 1)

while running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    prev = now
    now = pygame.mouse.get_pos()
    if prev != (0, 0):draw(prev, now)
    if prev == now : screen.fill("black")
    pygame.display.update()
pygame.quit()