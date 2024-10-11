#!/usr/bin/env python3


def checkmate(board):
    # Split the board into rows
    board = board.splitlines()
    n = len(board)

    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        print("Fail")
        return
    
    directions = {
        'R': [(0, 1), (1, 0), (0, -1), (-1, 0)],  # Rook moves: right, down, left, up
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop moves: diagonals
        'Q': [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  # Queen moves: all rook and bishop moves
        'P': [(-1, -1), (-1, 1)]  # Pawn captures diagonally upwards
    }
    
    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    def check_directions(piece, dirs):
        for dx, dy in dirs:
            x, y = king_pos[0] + dx, king_pos[1] + dy
            while is_in_bounds(x, y):
                if board[x][y] == 'K':
                    break
                if board[x][y] == piece:
                    return True
                if board[x][y] != '.':
                    break
                x, y = x + dx, y + dy
        return False

    for piece, dirs in directions.items():
        if piece == 'P':
            for dx, dy in directions['P']:
                x, y = king_pos[0] + dx, king_pos[1] + dy
                if is_in_bounds(x, y) and board[x][y] == 'P':
                    print("Success")
                    return
        else:
            if check_directions(piece, dirs):
                print("Success")
                return
    
    
    print("Fail")
