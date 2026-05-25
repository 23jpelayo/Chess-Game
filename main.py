import pygame as py, os, time

py.init()

screen = py.display.set_mode([400, 400])
WHITE = [255, 255, 255]
GREEN = [118, 150, 86]
BLACK = [0,0,0]


py.display.set_caption("Test1")
running = True
clock = py.time.Clock()
clock.tick(60)


# import chess pieces images
black_king = py.image.load("Pieces/Black King.svg").convert_alpha()
black_king = py.transform.scale(black_king, (50,50))
black_queen = py.image.load("Pieces/Black Queen.svg").convert_alpha()
black_queen = py.transform.scale(black_queen, (50,50))
black_bishop = py.image.load("Pieces/Black Bishop.svg").convert_alpha()
black_bishop = py.transform.scale(black_bishop, (50,50))
black_knight = py.image.load("Pieces/Black Knight.svg").convert_alpha()
black_knight = py.transform.scale(black_knight, (50,50))
black_rook = py.image.load("Pieces/Black Rook.svg").convert_alpha()
black_rook = py.transform.scale(black_rook, (50, 50))
black_pawn = py.image.load("Pieces/Black Pawn.svg").convert_alpha()
black_pawn = py.transform.scale(black_pawn, (50,50))
white_king = py.image.load("Pieces/White King.svg").convert_alpha()
white_king = py.transform.scale(white_king, (50, 50))
white_queen = py.image.load("Pieces/White Queen.svg").convert_alpha()
white_queen = py.transform.scale(white_queen, (50, 50))
white_bishop = py.image.load("Pieces/White Bishop.svg").convert_alpha()
white_bishop = py.transform.scale(white_bishop, (50, 50))
white_knight = py.image.load("Pieces/White Knight.svg").convert_alpha()
white_knight = py.transform.scale(white_knight, (50, 50))
white_rook = py.image.load("Pieces/White Rook.svg").convert_alpha()
white_rook = py.transform.scale(white_rook, (50, 50))
white_pawn = py.image.load("Pieces/White Pawn.svg").convert_alpha()
white_pawn = py.transform.scale(white_pawn, (50, 50))

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
# A
    A8 = py.draw.rect(screen, WHITE, (0, 0, 50, 50))
    A7 = py.draw.rect(screen, GREEN, (0, 50, 50, 50))
    A6 = py.draw.rect(screen, WHITE, (0, 100, 50, 50))
    A5 = py.draw.rect(screen, GREEN, (0, 150, 50, 50))
    A4 = py.draw.rect(screen, WHITE, (0, 200, 50, 50))
    A3 = py.draw.rect(screen, GREEN, (0, 250, 50, 50))
    A2 = py.draw.rect(screen, WHITE, (0, 300, 50, 50))
    A1 = py.draw.rect(screen, GREEN, (0, 350, 50, 50))
# B
    B8 = py.draw.rect(screen, GREEN, (50, 0, 50, 50))
    B7 = py.draw.rect(screen, WHITE, (50, 50, 50, 50))
    B6 = py.draw.rect(screen, GREEN, (50, 100, 50, 50))
    B5 = py.draw.rect(screen, WHITE, (50, 150, 50, 50))
    B4 = py.draw.rect(screen, GREEN, (50, 200, 50, 50))
    B3 = py.draw.rect(screen, WHITE, (50, 250, 50, 50))
    B2 = py.draw.rect(screen, GREEN, (50, 300, 50, 50))
    B1 = py.draw.rect(screen, WHITE, (50, 350, 50, 50))
# C
    C8 = py.draw.rect(screen, WHITE, (100, 0, 50, 50))
    C7 = py.draw.rect(screen, GREEN, (100, 50, 50, 50))
    C6 = py.draw.rect(screen, WHITE, (100, 100, 50, 50))
    C5 = py.draw.rect(screen, GREEN, (100, 150, 50, 50))
    C4 = py.draw.rect(screen, WHITE, (100, 200, 50, 50))
    C3 = py.draw.rect(screen, GREEN, (100, 250, 50, 50))
    C2 = py.draw.rect(screen, WHITE, (100, 300, 50, 50))
    C1 = py.draw.rect(screen, GREEN, (100, 350, 50, 50))
# D
    D8 = py.draw.rect(screen, GREEN, (150, 0, 50, 50))
    D7 = py.draw.rect(screen, WHITE, (150, 50, 50, 50))
    D6 = py.draw.rect(screen, GREEN, (150, 100, 50, 50))
    D5 = py.draw.rect(screen, WHITE, (150, 150, 50, 50))
    D4 = py.draw.rect(screen, GREEN, (150, 200, 50, 50))
    D3 = py.draw.rect(screen, WHITE, (150, 250, 50, 50))
    D2 = py.draw.rect(screen, GREEN, (150, 300, 50, 50))
    D1 = py.draw.rect(screen, WHITE, (150, 350, 50, 50))
# E
    E8 = py.draw.rect(screen, WHITE, (200, 0, 50, 50))
    E7 = py.draw.rect(screen, GREEN, (200, 50, 50, 50))
    E6 = py.draw.rect(screen, WHITE, (200, 100, 50, 50))
    E5 = py.draw.rect(screen, GREEN, (200, 150, 50, 50))
    E4 = py.draw.rect(screen, WHITE, (200, 200, 50, 50))
    E3 = py.draw.rect(screen, GREEN, (200, 250, 50, 50))
    E2 = py.draw.rect(screen, WHITE, (200, 300, 50, 50))
    E1 = py.draw.rect(screen, GREEN, (200, 350, 50, 50))
# F
    F8 = py.draw.rect(screen, GREEN, (250, 0, 50, 50))
    F7 = py.draw.rect(screen, WHITE, (250, 50, 50, 50))
    F6 = py.draw.rect(screen, GREEN, (250, 100, 50, 50))
    F5 = py.draw.rect(screen, WHITE, (250, 150, 50, 50))
    F4 = py.draw.rect(screen, GREEN, (250, 200, 50, 50))
    F3 = py.draw.rect(screen, WHITE, (250, 250, 50, 50))
    F2 = py.draw.rect(screen, GREEN, (250, 300, 50, 50))
    F1 = py.draw.rect(screen, WHITE, (250, 350, 50, 50))
# G
    G8 = py.draw.rect(screen, WHITE, (300, 0, 50, 50))
    G7 = py.draw.rect(screen, GREEN, (300, 50, 50, 50))
    G6 = py.draw.rect(screen, WHITE, (300, 100, 50, 50))
    G5 = py.draw.rect(screen, GREEN, (300, 150, 50, 50))
    G4 = py.draw.rect(screen, WHITE, (300, 200, 50, 50))
    G3 = py.draw.rect(screen, GREEN, (300, 250, 50, 50))
    G2 = py.draw.rect(screen, WHITE, (300, 300, 50, 50))
    G1 = py.draw.rect(screen, GREEN, (300, 350, 50, 50))
# H
    H8 = py.draw.rect(screen, GREEN, (350, 0, 50, 50))
    H7 = py.draw.rect(screen, WHITE, (350, 50, 50, 50))
    H6 = py.draw.rect(screen, GREEN, (350, 100, 50, 50))
    H5 = py.draw.rect(screen, WHITE, (350, 150, 50, 50))
    H4 = py.draw.rect(screen, GREEN, (350, 200, 50, 50))
    H3 = py.draw.rect(screen, WHITE, (350, 250, 50, 50))
    H2 = py.draw.rect(screen, GREEN, (350, 300, 50, 50))
    H1 = py.draw.rect(screen, WHITE, (350, 350, 50, 50))

    # load the chess pieces images
    screen.blit(black_king, (200, 0))
    screen.blit(black_queen, (150, 0))
    screen.blit(black_bishop, (250, 0))
    screen.blit(black_bishop, (100, 0))
    screen.blit(black_knight, (300, 0))
    screen.blit(black_knight, (50, 0))
    screen.blit(black_rook, (0, 0))
    screen.blit(black_rook, (350, 0))
    for i in range (8):
        screen.blit(black_pawn, (50*i, 50))
    screen.blit(white_king, (200, 350))

    screen.blit(white_king, (200, 350))
    screen.blit(white_queen, (150, 350))
    screen.blit(white_bishop, (250, 350))
    screen.blit(white_bishop, (100, 350))
    screen.blit(white_knight, (300, 350))
    screen.blit(white_knight, (50, 350))
    screen.blit(white_rook, (0, 350))
    screen.blit(white_rook, (350, 350))
    for i in range (8):
        screen.blit(white_pawn, (50*i, 300))

    py.display.flip()
    clock.tick(60)
