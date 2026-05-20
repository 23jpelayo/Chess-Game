import pygame as py, os, time

py.init()

screen = py.display.set_mode([400, 400])
WHITE = [255, 255, 255]
GREEN = [78, 120, 55]
BLACK = [0,0,0]


py.display.set_caption("Test1")
running = True
clock = py.time.Clock()
clock.tick(60)

object1 = py.Rect((20,50), (50, 150))

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill(BLACK)
# A
    py.draw.rect(screen, WHITE, (0, 0, 50, 50))
    py.draw.rect(screen, GREEN, (0, 50, 50, 50))
    py.draw.rect(screen, WHITE, (0, 100, 50, 50))
    py.draw.rect(screen, GREEN, (0, 150, 50, 50))
    py.draw.rect(screen, WHITE, (0, 200, 50, 50))
    py.draw.rect(screen, GREEN, (0, 250, 50, 50))
    py.draw.rect(screen, WHITE, (0, 300, 50, 50))
    py.draw.rect(screen, GREEN, (0, 350, 50, 50))
# B
    py.draw.rect(screen, GREEN, (50, 0, 50, 50))
    py.draw.rect(screen, WHITE, (50, 50, 50, 50))
    py.draw.rect(screen, GREEN, (50, 100, 50, 50))
    py.draw.rect(screen, WHITE, (50, 150, 50, 50))
    py.draw.rect(screen, GREEN, (50, 200, 50, 50))
    py.draw.rect(screen, WHITE, (50, 250, 50, 50))
    py.draw.rect(screen, GREEN, (50, 300, 50, 50))
    py.draw.rect(screen, WHITE, (50, 350, 50, 50))
# C
    py.draw.rect(screen, WHITE, (100, 0, 50, 50))
    py.draw.rect(screen, GREEN, (100, 50, 50, 50))
    py.draw.rect(screen, WHITE, (100, 100, 50, 50))
    py.draw.rect(screen, GREEN, (100, 150, 50, 50))
    py.draw.rect(screen, WHITE, (100, 200, 50, 50))
    py.draw.rect(screen, GREEN, (100, 250, 50, 50))
    py.draw.rect(screen, WHITE, (100, 300, 50, 50))
    py.draw.rect(screen, GREEN, (100, 350, 50, 50))
# D
    py.draw.rect(screen, GREEN, (150, 0, 50, 50))
    py.draw.rect(screen, WHITE, (150, 50, 50, 50))
    py.draw.rect(screen, GREEN, (150, 100, 50, 50))
    py.draw.rect(screen, WHITE, (150, 150, 50, 50))
    py.draw.rect(screen, GREEN, (150, 200, 50, 50))
    py.draw.rect(screen, WHITE, (150, 250, 50, 50))
    py.draw.rect(screen, GREEN, (150, 300, 50, 50))
    py.draw.rect(screen, WHITE, (150, 350, 50, 50))
# E
    py.draw.rect(screen, WHITE, (200, 0, 50, 50))
    py.draw.rect(screen, GREEN, (200, 50, 50, 50))
    py.draw.rect(screen, WHITE, (200, 100, 50, 50))
    py.draw.rect(screen, GREEN, (200, 150, 50, 50))
    py.draw.rect(screen, WHITE, (200, 200, 50, 50))
    py.draw.rect(screen, GREEN, (200, 250, 50, 50))
    py.draw.rect(screen, WHITE, (200, 300, 50, 50))
    py.draw.rect(screen, GREEN, (200, 350, 50, 50))
# F
    py.draw.rect(screen, GREEN, (250, 0, 50, 50))
    py.draw.rect(screen, WHITE, (250, 50, 50, 50))
    py.draw.rect(screen, GREEN, (250, 100, 50, 50))
    py.draw.rect(screen, WHITE, (250, 150, 50, 50))
    py.draw.rect(screen, GREEN, (250, 200, 50, 50))
    py.draw.rect(screen, WHITE, (250, 250, 50, 50))
    py.draw.rect(screen, GREEN, (250, 300, 50, 50))
    py.draw.rect(screen, WHITE, (250, 350, 50, 50))
# G
    py.draw.rect(screen, WHITE, (300, 0, 50, 50))
    py.draw.rect(screen, GREEN, (300, 50, 50, 50))
    py.draw.rect(screen, WHITE, (300, 100, 50, 50))
    py.draw.rect(screen, GREEN, (300, 150, 50, 50))
    py.draw.rect(screen, WHITE, (300, 200, 50, 50))
    py.draw.rect(screen, GREEN, (300, 250, 50, 50))
    py.draw.rect(screen, WHITE, (300, 300, 50, 50))
    py.draw.rect(screen, GREEN, (300, 350, 50, 50))
# H
    py.draw.rect(screen, GREEN, (350, 0, 50, 50))
    py.draw.rect(screen, WHITE, (350, 50, 50, 50))
    py.draw.rect(screen, GREEN, (350, 100, 50, 50))
    py.draw.rect(screen, WHITE, (350, 150, 50, 50))
    py.draw.rect(screen, GREEN, (350, 200, 50, 50))
    py.draw.rect(screen, WHITE, (350, 250, 50, 50))
    py.draw.rect(screen, GREEN, (350, 300, 50, 50))
    py.draw.rect(screen, WHITE, (350, 350, 50, 50))
    py.display.flip()
    clock.tick(60)
