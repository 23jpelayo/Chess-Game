import pygame as py, os, time

py.init()

HEIGHT = 400
WIDTH = 400

screen = py.display.set_mode((WIDTH, HEIGHT))
WHITE = [255, 255, 255]
GREEN = [118, 150, 86]

text_font = py.font.SysFont("Arial", 50)


py.display.set_caption("Test1")
running = True
clock = py.time.Clock()
clock.tick(60)


def draw_board():
    """Draw the board"""

    for row in range (8):
        for column in range (8):
            x = row * 50
            y = column * 50

            if (row + column) % 2 == 0:
                color = WHITE
            else:
                color = GREEN

            py.draw.rect(screen, color, (x, y, 50, 50))


def display_pieces():
    """Display the pieces on the board"""
    for row in range(8):
        for column in range(8):
            # checks for piece on the board
            piece = board[row][column]
            if piece != "Empty":
                screen.blit(images[piece], ((column*50), (row*50)))


def get_rook_moves(start_row, start_column, board, ally_pieces, enemy_king):
    """Get the valid squares the rook can move into"""
    valid_squares = []
    if enemy_king == "Black King":
        king = 'White King'
        piece = "White Rook"
    else:
        king = "Black King"
        piece = "Black Rook"

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # directions: up, down, left, right

    for r, c in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece

            elif board[row][column] not in ally_pieces and board[row][column] != enemy_king:
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
                break
            else:
                break

            row += r
            column += c      
    if len(valid_squares) > 0:
        return valid_squares
    else:
        return


def get_bishop_moves(start_row, start_column, board, ally_pieces, enemy_king):
    """Get the valid squares the bishop can move into"""
    valid_squares = []
    if enemy_king == "Black King":
        king = 'White King'
        piece = "White Bishop"
    else:
        king = "Black King"
        piece = "Black Bishop"

    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    # directions: up-right, up-left, down-right, down-left

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
            elif board[row][column] not in ally_pieces and board[row][column] != enemy_king:
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
                break
            else:
                break

            row += r
            column += c

    if len(valid_squares) > 0:
        return valid_squares
    else:
        return


def get_queen_moves(start_row, start_column, board, ally_pieces, enemy_king):
    """Get the valid squares the queen can move into"""
    valid_squares = []
    if enemy_king == "Black King":
        king = 'White King'
        piece = "White Queen"
    else:
        king = "Black King"
        piece = "Black Queen"

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
    # directions: up, down, left, right, up-right, up-left, down-right, down-left

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        while -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
            elif board[row][column] not in ally_pieces and board[row][column] != enemy_king:
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
                break
            else:
                break

            row += r
            column += c

    if len(valid_squares) > 0:
        return valid_squares
    else:
        return


def get_pawn_moves(start_row, start_column, board, ally_piece, enemy_king):
    """Get the valid squares the pawn can move into"""
    valid_squares = []
    if enemy_king == "Black King":
        king = 'White King'
        piece = "White Pawn"
    else:
        king = "Black King"
        piece = "Black Pawn"

    if board[start_row][start_column] == "White Pawn":
        forward_direction = -1
        starting_rank = 6
    else:
        forward_direction = 1
        starting_rank = 1

    move_row = start_row + forward_direction
    if -1 < move_row < 8:
        if board[move_row][start_column] == "Empty":
            destination_square = board[move_row][start_column]
            move_sprite(board, move_row, start_column, start_row, start_column, piece)
            if scan_check(board, king) == False:
                valid_squares.append((move_row, start_column))

            board[move_row][start_column] = destination_square
            board[start_row][start_column] = piece

        move_row_twice = start_row + (forward_direction * 2)
        if start_row == starting_rank and -1 < move_row_twice < 8:
            if board[move_row_twice][start_column] == "Empty" and board[move_row][start_column] == "Empty":
                destination_square = board[move_row_twice][start_column]
                move_sprite(board, move_row_twice, start_column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((move_row_twice, start_column))

                board[move_row_twice][start_column] = destination_square
                board[start_row][start_column] = piece

    capture_moves = [(forward_direction, -1), (forward_direction, 1)]
    for r, c in capture_moves:
        row = start_row + r
        column = start_column + c

        if -1 < row < 8 and -1 < column < 8:
            if board[row][column] != "Empty" and board[row][column] not in ally_piece and board[row][column] != enemy_king:
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece

    if len(valid_squares) > 0:
        return valid_squares
    else:
        return


def get_king_moves(start_row, start_column, board, ally_pieces, enemy_king):
    """Get the valid squares the king can move into"""
    valid_squares = []
    if enemy_king == "Black King":
        king = 'White King'
        piece = "White King"
    else:
        king = "Black King"
        piece = "Black King"

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
    # directions: up, down, left, right, up-right, up-left, down-right, down-left

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        if -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
            elif board[row][column] not in ally_pieces and board[row][column] != enemy_king:
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece

    if len(valid_squares) > 0:
        return valid_squares
    else:
        return


def get_knight_moves(start_row, start_column, board, ally_pieces, enemy_king):
    """Get the valid squares the knight can move into"""
    valid_squares = []
    if enemy_king == "Black King":
        king = 'White King'
        piece = "White Knight"
    else:
        king = "Black King"
        piece = "Black Knight"

    directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
                  (-1, -2), (-1, 2), (1, -2), (1, 2)]
    # directions: (2-up 1-left), (2-up 1-right), (2-down 1-left), (2-down 1-right)
    # directions: (1-up 2-left), (1-up 2-right), (1-down, 2-left), (1-down 2-right)

    for r, c, in directions:
        row = start_row + r
        column = start_column + c

        if -1 < row < 8 and -1 < column < 8:
            if board[row][column] == "Empty":
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece
            elif board[row][column] not in ally_pieces and board[row][column] != enemy_king:
                destination_square = board[row][column]
                move_sprite(board, row, column, start_row, start_column, piece)
                if scan_check(board, king) == False:
                    valid_squares.append((row, column))

                board[row][column] = destination_square
                board[start_row][start_column] = piece

    if len(valid_squares) > 0:
        return valid_squares
    else:
        return


def move_sprite(board, click_row, click_column, start_row, start_column, move_piece):
    board[click_row][click_column] = move_piece
    if (click_row, click_column) != (start_row, start_column):
        board[start_row][start_column] = "Empty"


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
        enemy_king = "Black King"
        enemy_rook = "Black Rook"
        enemy_knight = "Black Knight"
        enemy_bishop = "Black Bishop"
        enemy_queen = "Black Queen"
        enemy_pawn = "Black Pawn"
        pawn_row = -1 
        # white king looks for pawns above its row
    else:
        enemy_king = "White King"
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
            if (start_row - 2) < row < (start_row + 2) and (start_column - 2) < column < (start_column + 2):
                if board[row][column] == enemy_king:
                    return True
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
            if (start_row - 2) < row < (start_row + 2) and (start_column - 2) < column < (start_column + 2):
                if board[row][column] == enemy_king:
                    return True
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


def scan_checkmate(board, black_pieces, white_pieces, turn):
    valid_moves = []
    if turn == "White":
        king = "White King"
        enemy_king = "Black King"
        ally_piece = white_pieces
    else:
        king = "Black King"
        enemy_king = "White King"
        ally_piece = black_pieces
        
    if scan_check(board, king) is True:
        for piece in ally_piece:
            for row in range(8):
                for column in range(8):
                    if board[row][column] == piece:
                        if piece == ally_piece[0]:
                            if get_king_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_king_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[1]:
                            if get_queen_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_queen_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[2]:
                            if get_bishop_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_bishop_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[3]:
                            if get_knight_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_knight_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[4]:
                            if get_rook_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_rook_moves(row, column, board, ally_piece, enemy_king))
                        else:
                            if get_pawn_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_pawn_moves(row, column, board, ally_piece, enemy_king))

        if valid_moves == []:
            return True
        else:
            return False
                    
def scan_stalemate(board, black_pieces, white_pieces, turn):
    valid_moves = []
    if turn == "White":
        king = "White King"
        enemy_king = "Black King"
        ally_piece = white_pieces
    else:
        king = "Black King"
        enemy_king = "White King"
        ally_piece = black_pieces

    if scan_check(board, king) is False:
        for piece in ally_piece:
            for row in range(8):
                for column in range(8):
                    if board[row][column] == piece:
                        if piece == ally_piece[0]:
                            if get_king_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_king_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[1]:
                            if get_queen_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_queen_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[2]:
                            if get_bishop_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_bishop_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[3]:
                            if get_knight_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_knight_moves(row, column, board, ally_piece, enemy_king))
                        elif piece == ally_piece[4]:
                            if get_rook_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_rook_moves(row, column, board, ally_piece, enemy_king))
                        else:
                            if get_pawn_moves(row, column, board, ally_piece, enemy_king) is not None:
                                valid_moves.extend(get_pawn_moves(row, column, board, ally_piece, enemy_king))

        if valid_moves == []:
            return True
        else:
            return False


def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color, "white")
    screen.blit(image, (x, y))

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
valid_moves = []
turn = "White"

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
                    if (turn == 'White' and piece in white_pieces) or (turn == 'Black' and piece in black_pieces):
                        clicked_square = (clicked_row, clicked_column)

                        match piece:
                            case "White Rook":
                                valid_moves = get_rook_moves(clicked_row, clicked_column, board, white_pieces, "Black King")
                            case "White Pawn":
                                valid_moves = get_pawn_moves(clicked_row, clicked_column, board, white_pieces, "Black King")
                            case "White Bishop":
                                valid_moves = get_bishop_moves(clicked_row, clicked_column, board, white_pieces, "Black King")
                            case "White Queen":
                                valid_moves = get_queen_moves(clicked_row, clicked_column, board, white_pieces, "Black King")
                            case "White Knight":
                                valid_moves = get_knight_moves(clicked_row, clicked_column, board, white_pieces, "Black King")
                            case "White King":
                                valid_moves = get_king_moves(clicked_row, clicked_column, board, white_pieces, "Black King")
                            case "Black Rook":
                                valid_moves = get_rook_moves(clicked_row, clicked_column, board, black_pieces, "White King")
                            case "Black Pawn":
                                valid_moves = get_pawn_moves(clicked_row, clicked_column, board, black_pieces, "White King")
                            case "Black Bishop":
                                valid_moves = get_bishop_moves(clicked_row, clicked_column, board, black_pieces, "White King")
                            case "Black Queen":
                                valid_moves = get_queen_moves(clicked_row, clicked_column, board, black_pieces, "White King")
                            case "Black Knight":
                                valid_moves = get_knight_moves(clicked_row, clicked_column, board, black_pieces, "White King")
                            case "Black King":
                                valid_moves = get_king_moves(clicked_row, clicked_column, board, black_pieces, "White King")

            else:
                # After the second click, the previous location of the piece is stored in starting_row and swtarting_column
                starting_row, starting_column = clicked_square

                move_piece = board[starting_row][starting_column]
                move_made = False

                # Pawn movement
                if move_piece == "White Pawn" or move_piece == "Black Pawn" :
                    if move_piece == "White Pawn":
                        enemy_king = "Black King"
                        valid_squares = get_pawn_moves(starting_row, starting_column, board, white_pieces, enemy_king)
                    else:
                        enemy_king = "White King"
                        valid_squares = get_pawn_moves(starting_row, starting_column, board, black_pieces, enemy_king)

                    if valid_squares is not None and (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                        move_made = True

                # Rook movement
                if move_piece == "White Rook" or move_piece == "Black Rook":
                    if move_piece == "White Rook":
                        king = "White King"
                        enemy_king = "Black King"
                        valid_squares = get_rook_moves(starting_row, starting_column, board, white_pieces, enemy_king)
                    else:
                        king = "Black King"
                        enemy_king = 'White King'
                        valid_squares = get_rook_moves(starting_row, starting_column, board, black_pieces, enemy_king)

                    if valid_squares is not None and (clicked_row, clicked_column) in valid_squares:
                        destination_square = board[clicked_row][clicked_column]
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                        move_made = True

                # Bishop movement 
                if move_piece == "White Bishop" or move_piece == "Black Bishop":
                    if move_piece == "White Bishop":
                        king = "White King"
                        enemy_king = "Black King"
                        valid_squares = get_bishop_moves(starting_row, starting_column, board, white_pieces, enemy_king)
                    else:
                        king = 'Black King'
                        enemy_king = "White King"
                        valid_squares = get_bishop_moves(starting_row, starting_column, board, black_pieces, enemy_king)
                    if valid_squares is not None and (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                        move_made = True

                # Queen movement
                if move_piece == "White Queen" or move_piece == "Black Queen":
                    if move_piece == "White Queen":
                        king = 'White King'
                        enemy_king = "Black King"
                        valid_squares = get_queen_moves(starting_row, starting_column, board, white_pieces, enemy_king)
                    else:
                        king = 'Black King'
                        enemy_king = "White King"
                        valid_squares = get_queen_moves(starting_row, starting_column, board, black_pieces, enemy_king)

                    if valid_squares is not None and (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                        move_made = True

                # King movement
                if move_piece == "White King" or move_piece == "Black King":
                    if move_piece == "White King":
                        king = 'White King'
                        enemy_king = "Black King"
                        valid_squares = get_king_moves(starting_row, starting_column, board, white_pieces, enemy_king)
                    else:
                        king = 'Black King'
                        enemy_king = "White King"
                        valid_squares = get_king_moves(starting_row, starting_column, board, black_pieces, enemy_king)

                    if valid_squares is not None and (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                        move_made = True

                # Knight movement
                if move_piece == "White Knight" or move_piece == "Black Knight":
                    if move_piece == "White Knight":
                        king = 'White King'
                        enemy_king = "Black King"
                        valid_squares = get_knight_moves(starting_row, starting_column, board, white_pieces, enemy_king)
                    else:
                        king = 'Black King'
                        enemy_king = "White King"
                        valid_squares = get_knight_moves(starting_row, starting_column, board, black_pieces, enemy_king)

                    if valid_squares is not None and (clicked_row, clicked_column) in valid_squares:
                        move_sprite(board, clicked_row, clicked_column, starting_row, starting_column, move_piece)
                        move_made = True

                if move_made:
                    if turn == "White":
                        turn = "Black"
                    else:
                        turn = "White"

                clicked_square = None
                if valid_moves is not None:
                    valid_moves.clear()

    draw_board()

    display_pieces()
    if valid_moves is not None:
        for r, c in valid_moves:
            center_x = (c * 50) + 25
            center_y = (r * 50) + 25

            py.draw.circle(screen, "grey", (center_x, center_y), 8)

    if scan_checkmate(board, black_pieces, white_pieces, turn) == True:
        if turn == "White":
            draw_text("Black Wins", text_font, "black", 150, 150)
        else:
            draw_text("White Wins", text_font, "black", 150, 150)

    elif scan_stalemate(board, black_pieces, white_pieces, turn) == True:
        draw_text("Draw", text_font, "black", 150, 150)


    py.display.flip()
    clock.tick(60)

