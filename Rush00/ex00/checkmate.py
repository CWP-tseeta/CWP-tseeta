PIECES = "RBQPK"
 
def parse_board(board):
    if not board:
        return None
 
    lines = board.split('\n')
    if lines and lines[-1] == "":
        lines.pop()
 
    if not lines:
        return None
 
    size = len(lines)
    for line in lines:
        if len(line) != size:
            return None
 
    return lines
 
def find_king(grid):
    king = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'K':
                if king is not None:
                    return None
                king = (r, c)
    return king
 
def path_is_clear(grid, r, c, kr, kc, rstep, cstep):
    rr, cc = r + rstep, c + cstep
    while (rr, cc) != (kr, kc):
        if grid[rr][cc] in PIECES:
            return False
        rr += rstep
        cc += cstep
    return True
 
def rook_threatens(grid, r, c, kr, kc):
    if r != kr and c != kc:
        return False
    rstep = 0 if r == kr else (1 if kr > r else -1)
    cstep = 0 if c == kc else (1 if kc > c else -1)
    return path_is_clear(grid, r, c, kr, kc, rstep, cstep)
 
def bishop_threatens(grid, r, c, kr, kc):
    if r == kr or abs(kr - r) != abs(kc - c):
        return False
    rstep = 1 if kr > r else -1
    cstep = 1 if kc > c else -1
    return path_is_clear(grid, r, c, kr, kc, rstep, cstep)
 
def queen_threatens(grid, r, c, kr, kc):
    return rook_threatens(grid, r, c, kr, kc) or bishop_threatens(grid, r, c, kr, kc)
 
def pawn_threatens(r, c, kr, kc):
    return kr == r - 1 and abs(kc - c) == 1
 
def checkmate(board):
    grid = parse_board(board)
    if grid is None:
        return
 
    king_pos = find_king(grid)
    if king_pos is None:
        return
 
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