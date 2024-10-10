def create_board():
    return [["." for _ in range(8)] for _ in range(8)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def add_white_pieces(board):
    board[6][4] = 'P'  # White pawn
    board[7][4] = 'K'  # White king

def add_black_pieces(board):
    board[1][4] = 'p'  # Black pawn
    board[0][4] = 'k'  # Black king

def move_piece(board, start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]
    board[start_row][start_col] = "."
    board[end_row][end_col] = piece

def is_checkmate(board, king):
    king_pos = None
    for row in range(8):
        for col in range(8):
            if board[row][col] == king:
                king_pos = (row, col)
                break
        if king_pos:
            break

    if not king_pos:
        return False

    row, col = king_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == ".":
            return False

    return True

def main():
    board = create_board()
    
    # Add white and black pieces
    add_white_pieces(board)
    add_black_pieces(board)

    print("Initial Board:")
    print_board(board)

    # Example move (King to a new position)
    move_piece(board, (7, 4), (6, 4))
    print("\nAfter Move:")
    print_board(board)

    if is_checkmate(board, 'K'):
        print("Checkmate! Game over.")
    else:
        print("Game continues.")

if __name__ == "__main__":
    main()
