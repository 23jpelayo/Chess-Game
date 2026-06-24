import pygame as py, os, time

py.init()

HEIGHT = 400
WIDTH = 400

screen = py.display.set_mode((WIDTH, HEIGHT))
WHITE = [255, 255, 255]
GREEN = [118, 150, 86]


py.display.set_caption("Test1")
running = True
clock = py.time.Clock()
clock.tick(60)


def draw_board():
    """Draw the board"""
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


def display_pieces():
    """Display the pieces on the board"""
    for row in range(8):
        for column in range(8):
            # checks for piece on the board
            piece = board[row][column]
            if piece != "Empty":
                screen.blit(images[piece], ((column*50), (row*50)))


def get_rook_moves(start_row, start_column, board, ally_pieces):
    """Get the valid squares the rook can move into"""
    valid_squares = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # directions: up, down, left, right

    for r, c in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                valid_squares.append((row, column))
            elif board[row][column] not in ally_pieces:
                valid_squares.append((row, column))
                break
            else:
                break

            row += r
            column += c

    return valid_squares


def get_bishop_moves(start_row, start_column, board, ally_pieces):
    """Get the valid squares the bishop can move into"""
    valid_squares = []

    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    # directions: up-right, up-left, down-right, down-left

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                valid_squares.append((row, column))
            elif board[row][column] not in ally_pieces:
                valid_squares.append((row, column))
                break
            else:
                break

            row += r
            column += c

    return valid_squares


def get_queen_moves(start_row, start_column, board, ally_pieces):
    """Get the valid squares the queen can move into"""
    valid_squares = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
    # directions: up, down, left, right, up-right, up-left, down-right, down-left

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                valid_squares.append((row, column))
            elif board[row][column] not in ally_pieces:
                valid_squares.append((row, column))
                break
            else:
                break

            row += r
            column += c

    return valid_squares


def get_pawn_moves(start_row, start_column, board, ally_piece):
    """Get the valid squares the pawn can move into"""
    valid_squares = []

    if board[start_row][start_column] == "White Pawn":
        forward_direction = -1
        starting_rank = 6
    else:
        forward_direction = 1
        starting_rank = 1

    move_row = start_row + forward_direction
    if -1 < move_row < 8:
        if board[move_row][start_column] == "Empty":
            valid_squares.append((move_row, start_column))

        move_row_twice = starting_row + (forward_direction * 2)
        if start_row == starting_rank and -1 < move_row_twice < 8:
            if board[move_row_twice][start_column] == "Empty":
                valid_squares.append((move_row_twice, start_column))

    capture_moves = [(forward_direction, -1), (forward_direction, 1)]
    for r, c in capture_moves:
        row = start_row + r
        column = start_column + c

        if -1 < row < 8 and -1 < column < 8:
            if board[row][column] != "Empty" and board[row][column] not in ally_piece:
                valid_squares.append((row, column))

    return valid_squares

def get_king_moves(start_row, start_column, board, ally_pieces):
    """Get the valid squares the king can move into"""
    valid_squares = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
    # directions: up, down, left, right, up-right, up-left, down-right, down-left

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                valid_squares.append((row, column))
            elif board[row][column] not in ally_pieces:
                valid_squares.append((row, column))
                break
            else:
                break

            row += r
            column += c

    return valid_squares


def get_knight_moves(start_row, start_column, board, ally_pieces):
    """Get the valid squares the knight can move into"""
    valid_squares = []

    directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
                  (-1, -2), (-1, 2), (1, -2), (1, 2)]
    # directions: (2-up 1-left), (2-up 1-right), (2-down 1-left), (2-down 1-right)
    # directions: (1-up 2-left), (1-up 2-right), (1-down, 2-left), (1-down 2-right)

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                valid_squares.append((row, column))
            elif board[row][column] not in ally_pieces:
                valid_squares.append((row, column))
                break
            else:
                break

            row += r
            column += c

    return valid_squares

def move_sprite(board, click_row, click_column, start_row, start_column, move_piece):
    board[click_row][click_column] = move_piece
    if (click_row, click_column) != (start_row, start_column):
        board[starting_row][starting_column] = "Empty"

def find_king(board, king_color):

    if king_color == "White King":
        for row in range(8):
            for column in range(8):
                if board[row][column] == "White King":
                    return((row, column))
    elif king_color == "Black King":
        for row in range(8):
            for column in range(8):
                if board[row][column] == "Black King":
                    return((row, column))
                
def scan_check(board, king_color):
    king_square = find_king(board, king_color)

    start_row, start_column = king_square

    if king_color == "White King":
        enemy_rook = "Black Rook"
        enemy_knight = "Black Knight"
        enemy_bishop = "Black Bishop"
        enemy_queen = "Black Queen"
        enemy_pawn = "Black Pawn"
        pawn_row = -1 
        # white king looks for pawns above its row
    else:
        enemy_rook = "White Rook"
        enemy_knight = "White Knight"
        enemy_bishop = "White Bishop"
        enemy_queen = "White Queen"
        enemy_pawn = "White Pawn"
        pawn_row = 1
        # black king looks for pawns below its row

    vertical_horizontal_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # up, down, left, right
    for r, c in vertical_horizontal_direction: 
        row = start_row + r
        column = start_column + c
        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] != "Empty":
                if board[row][column] == enemy_rook or board[row][column] == enemy_queen:
                    return True
                break
            row += r
            column += c

    diagonal_direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # up-left, up-right, down-left, down-right

    for r, c in diagonal_direction:
        row = start_row + r
        column = start_column + c
        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] != "Empty":
                if board[row][column] == enemy_bishop or board[row][column] == enemy_queen:
                    return True
                break
            row += r
            column += c
            

    knight_directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    # directions: (2-up 1-left), (2-up 1-right), (2-down 1-left), (2-down 1-right)
    # directions: (1-up 2-left), (1-up 2-right), (1-down, 2-left), (1-down 2-right)

    for r, c in knight_directions:
            row = start_row + r
            column = start_column + c
            if -1 < row < 8 and -1 < column < 8:
                if board[row][column] != "Empty":
                    if board[row][column] == enemy_knight:
                        return True
            

    pawn_attack = [(pawn_row, -1), (pawn_row, 1)]
    for r, c in pawn_attack:
        row = start_row + r
        column = start_column + c
        if 0 <= row < 8 and 0 <= column < 8:
            if board[row][column] == enemy_pawn:
                return True

    return False



# position of pieces on the board
board = [
    ["Black Rook", "Black Knight", "Black Bishop", "Black Queen", "Black King", "Black Bishop", "Black Knight", "Black Rook"],
    ["Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn",],
    ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty",],
    ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty",],
    ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty",],
    ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty",],
    ["White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn",],
    ["White Rook", "White Knight", "White Bishop", "White Queen", "White King", "White Bishop", "White Knight", "White Rook"]
]
# import chess pieces images

images = {}
black_pieces = ["Black King", "Black Queen", "Black Bishop", "Black Knight", "Black Rook", "Black Pawn"]
white_pieces = ["White King", "White Queen", "White Bishop", "White Knight", "White Rook", "White Pawn"]
filename = {
    "Black King" : "Pieces/Black King.svg",
    "Black Queen" : "Pieces/Black Queen.svg",
    "Black Bishop" : "Pieces/Black Bishop.svg",
    "Black Knight" : "Pieces/Black Knight.svg",
    "Black Rook" : "Pieces/Black Rook.svg",
    "Black Pawn" : "Pieces/Black Pawn.svg",
    "White King" : "Pieces/White King.svg",
    "White Queen" : "Pieces/White Queen.svg",
    "White Bishop" : "Pieces/White Bishop.svg",
    "White Knight" : "Pieces/White Knight.svg",
    "White Rook" : "Pieces/White Rook.svg",
    "White Pawn" : "Pieces/White Pawn.svg"
}

for piece in black_pieces:
    images[piece] = py.image.load(filename[piece]).convert_alpha()
    images[piece] = py.transform.scale(images[piece], (50, 50))

for piece in white_pieces:
    images[piece] = py.image.load(filename[piece]).convert_alpha()
    images[piece] = py.transform.scale(images[piece], (50, 50))

clicked_square = None

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        elif event.type == py.MOUSEBUTTONDOWN:
            
            x_pos, y_pos = py.mouse.get_pos()

            clicked_column = x_pos // 50
            clicked_row = y_pos // 50

            if clicked_square is None:
                piece = board[clicked_row][clicked_column]

                if piece != "Empty":
                    clicked_square = (clicked_row, clicked_column)

            else:
                # After the second click, the previous location of the piece is stored in starting_row and swtarting_column
                starting_row, starting_column = clicked_square

                move_piece = board[starting_row][starting_column]

                # Pawn movement
                if move_piece == "White Pawn" or move_piece == "Black Pawn" :
                    if move_piece == "White Pawn":
                        valid_squares = get_pawn_moves(starting_row, starting_column, board, white_pieces)
                    else:
                        valid_squares = get_pawn_moves(starting_row, starting_column, board, black_pieces)

                    if (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)

                # Rook movement
                if move_piece == "White Rook" or move_piece == "Black Rook":
                    if move_piece == "White Rook":
                        king = "White King"
                        valid_squares = get_rook_moves(starting_row, starting_column, board, white_pieces)
                    else:
                        king = "Black King"
                        valid_squares = get_rook_moves(starting_row, starting_column, board, black_pieces)

                    if (clicked_row, clicked_column) in valid_squares:
                        if scan_check(board, king) == False:
                            move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)


                # Bishop movement 
                if move_piece == "White Bishop" or move_piece == "Black Bishop":
                    if move_piece == "White Bishop":
                        valid_squares = get_bishop_moves(starting_row, starting_column, board, white_pieces)
                    else:
                        valid_squares = get_bishop_moves(starting_row, starting_column, board, black_pieces)
                    if (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)

                # Queen movement
                if move_piece == "White Queen" or move_piece == "Black Queen":
                    if move_piece == "White Queen":
                        valid_squares = get_queen_moves(starting_row, starting_column, board, white_pieces)
                    else:
                        valid_squares = get_queen_moves(starting_row, starting_column, board, black_pieces)

                    if (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)

                # King movement
                if move_piece == "White King" or move_piece == "Black King":
                    if move_piece == "White King":
                        valid_squares = get_king_moves(starting_row, starting_column, board, white_pieces)
                    else:
                        valid_squares = get_king_moves(starting_row, starting_column, board, black_pieces)

                    if (clicked_row, clicked_column) in valid_squares:
                        if clicked_row == starting_row + 1 or clicked_row == starting_row - 1 or clicked_column == starting_column + 1 or clicked_column == starting_column - 1:
                            if move_piece == "White King":
                                if board[clicked_row][clicked_column] not in white_pieces:
                                    move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                            else:
                                if board[clicked_row][clicked_column] not in black_pieces:
                                    move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)

                # Knight movement
                if move_piece == "White Knight" or move_piece == "Black Knight":
                    if move_piece == "White Knight":
                        valid_squares = get_knight_moves(starting_row, starting_column, board, white_pieces)
                    else:
                        valid_squares = get_knight_moves(starting_row, starting_column, board, black_pieces)

                    if (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)

                clicked_square = None

    draw_board()

    display_pieces()

    py.display.flip()
    clock.tick(60)
