#!/usr/bin/env python3

def checkmate(board_str):
    # Parse the board from the string
    board = [list(row) for row in board_str.splitlines()]
    size = len(board)  # The board is a square, so height equals width
    
    # Find the King's position
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        return  # No King found, undefined behavior
    
    king_x, king_y = king_pos

    # Define the directions in which pieces can move
    directions = {
        'R': [(1, 0), (-1, 0), (0, 1), (0, -1)],  # Rook (horizontal/vertical)
        'B': [(1, 1), (-1, -1), (1, -1), (-1, 1)],  # Bishop (diagonal)
        'Q': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],  # Queen (Rook + Bishop)
        'P': [(-1, -1), (-1, 1)]  # Pawn (attacks diagonally upwards to the King)
    }

    # Helper function to check if the King is in check from a particular direction
    def is_in_check_from_direction(x, y, dx, dy, piece):
        while 0 <= x < size and 0 <= y < size:
            x += dx
            y += dy
            if not (0 <= x < size and 0 <= y < size):
                break
            if board[x][y] == 'K':  # King found
                return True
            if board[x][y] != '.':  # Piece blocking the path
                break
        return False

    # Check for threats from each enemy piece
    for i in range(size):
        for j in range(size):
            piece = board[i][j]
            if piece in directions:
                # Check all directions the piece can move
                for dx, dy in directions[piece]:
                    if is_in_check_from_direction(i, j, dx, dy, piece):
                        return "Success"

            # Special case for Pawn
            if piece == 'P':
                for dx, dy in directions['P']:
                    px, py = i + dx, j + dy
                    if 0 <= px < size and 0 <= py < size and (px, py) == king_pos:
                        return "Success"

    # If no threats found
    return "Fail"

# This function will run when checkmate.py is executed directly
def main():
    # Example 1
    board1 = """\
R...
.K..
..P.
....\
"""
    result1 = checkmate(board1)
    print(result1)  # Should print "Success"

    # Example 2
    board2 = """\
..
.K\
"""
    result2 = checkmate(board2)
    print(result2)  # Should print "Fail"

# Entry point: if this file is executed directly, run the main function
if __name__ == "__main__":
    main()
