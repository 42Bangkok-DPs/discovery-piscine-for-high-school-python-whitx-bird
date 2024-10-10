#!/usr/bin/env python3

# Import the checkmate function from the checkmate.py file
from checkmate import checkmate

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

if __name__ == "__main__":
    main()
