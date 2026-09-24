"""checkmate.py
 
Contains the checkmate() function: given a chessboard (as a multi-line
string), it prints "Success" if the King is currently threatened
("in check") by any other piece, or "Fail" otherwise.
"""
 
# The only characters we recognize as actual chess pieces.
# Anything else on the board (dots, spaces, letters we don't know...)
# is treated as an empty square.
PIECES = "RBQPK"
 
 
def parse_board(board):
    """Turn the raw board string into a list of row-strings.
 
    Returns None if the board is not a proper square (rows of
    different lengths, or the number of rows doesn't match the
    number of columns) -> this is our "undefined behavior" guard.
    """
    if not board:
        return None
 
    lines = board.split('\n')
    # A trailing newline in the input produces one extra empty
    # element at the end of the list; drop it if present.
    if lines and lines[-1] == "":
        lines.pop()
 
    if not lines:
        return None
 
    size = len(lines)
    for line in lines:
        if len(line) != size:
            return None  # not a square board -> invalid
 
    return lines
 
 
def find_king(grid):
    """Return the (row, col) of the single King on the board.
 
    Returns None if there is no King, or if there is more than one
    (both are considered invalid boards).
    """
    king = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'K':
                if king is not None:
                    return None  # more than one King
                king = (r, c)
    return king
 
 
def path_is_clear(grid, r, c, kr, kc, rstep, cstep):
    """Walk from (r, c) towards (kr, kc) one step at a time (rstep,
    cstep) and make sure every square in between (NOT including the
    piece itself or the King's square) is empty of pieces.
    """
    rr, cc = r + rstep, c + cstep
    while (rr, cc) != (kr, kc):
        if grid[rr][cc] in PIECES:
            return False  # something is blocking the path
        rr += rstep
        cc += cstep
    return True
 
 
def rook_threatens(grid, r, c, kr, kc):
    """A Rook threatens the King if they share a row or a column,
    and nothing stands between them."""
    if r != kr and c != kc:
        return False
    rstep = 0 if r == kr else (1 if kr > r else -1)
    cstep = 0 if c == kc else (1 if kc > c else -1)
    return path_is_clear(grid, r, c, kr, kc, rstep, cstep)
 
 
def bishop_threatens(grid, r, c, kr, kc):
    """A Bishop threatens the King if they're on the same diagonal,
    and nothing stands between them."""
    if r == kr or abs(kr - r) != abs(kc - c):
        return False
    rstep = 1 if kr > r else -1
    cstep = 1 if kc > c else -1
    return path_is_clear(grid, r, c, kr, kc, rstep, cstep)
 
 
def queen_threatens(grid, r, c, kr, kc):
    """A Queen moves like a Rook AND a Bishop combined."""
    return rook_threatens(grid, r, c, kr, kc) or bishop_threatens(grid, r, c, kr, kc)
 
 
def pawn_threatens(r, c, kr, kc):
    """A Pawn only threatens the square diagonally one row 'above'
    it (one row up, one column left or right), as shown in the
    subject's diagram. It has no blocking to check since the range
    is fixed at one square."""
    return kr == r - 1 and abs(kc - c) == 1
 
 
def checkmate(board):
    """Print 'Success' if the King on `board` is in check,
    'Fail' otherwise. Silently returns on malformed input."""
    grid = parse_board(board)
    if grid is None:
        return  # undefined behavior: give back control, print nothing
 
    king_pos = find_king(grid)
    if king_pos is None:
        return  # no King, or more than one -> undefined behavior
 
    kr, kc = king_pos
 
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if (r, c) == (kr, kc):
                continue
            if ch == 'R' and rook_threatens(grid, r, c, kr, kc):
                print("Success")
                return
            if ch == 'B' and bishop_threatens(grid, r, c, kr, kc):
                print("Success")
                return
            if ch == 'Q' and queen_threatens(grid, r, c, kr, kc):
                print("Success")
                return
            if ch == 'P' and pawn_threatens(r, c, kr, kc):
                print("Success")
                return
 
    print("Fail")