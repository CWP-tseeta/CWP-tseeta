PIECES = "RBQPK" #กำหนดตัวหมาก

def parse_board(board_text):
    lines = board_text.split('\n') #ขึ้นบรรทัดใหม่ที่ \n

    if lines[-1] == "":
        lines = lines[:-1] #ป้องกันการขึ้นบรรทัดใหม่เนื่องจาก \n ที่ต่อท้ายหลังสุด

    size = len(lines)
    for line in lines: #ตรวจสอบความเป็นจัตุรัสของกระดาน
        if len(line) != size:
            return None

    return lines

def find_king(board): #หา king
    king_row = -1
    king_col = -1
    #ให้เป็น -1 เพื่อใช้ตรวจสอบว่ามี king อยู่ในกระดานหรือไม่

    for row in range(len(board)): #หา row ที่มี king
        for col in range(len(board[row])): #หา column ที่มี king
            if board[row][col] == 'K':
                if king_row != -1:
                    return -1, -1 #สั่งหยุดการทำงานเนื่องจากเจอ king ตัวที่ 2
                king_row = row #กำหนดค่า row ของ king ใหม่
                king_col = col #กำหนดค่า column ของ king ใหม่

    return king_row, king_col

def is_path_clear(board, row, col, king_row, king_col, drow, dcol):
    row = row + drow
    col = col + dcol
    #ขยับตำแหน่งไปข้างหน้า 1 ก้าว ตามทิศทางที่กำหนด เพื่อป้องกันไม่ให้ตรวจสอบตำแหน่งของตัวหมากเอง
    while row != king_row or col != king_col:
        if board[row][col] in PIECES:
            return False #สั่งหยุดการทำงานเนื่องจากเจอหมากตัวอื่นขวางทาง
        row = row + drow
        col = col + dcol
        #ขยับตำแหน่งไปข้างหน้า 1 ก้าว ตามทิศทางที่กำหนด
    return True

def rook_moves(board, row, col, king_row, king_col): #ตาเดินของ Rook
    if row != king_row and col != king_col:
        return False

    if row == king_row: #R อยู่ row เดียวกับ king
        drow = 0 #ไม่ต้องขยับ row
        if col < king_col:
            dcol = 1 #ขยับ column ไปทางขวา
        else:
            dcol = -1 #ขยับ column ไปทางซ้าย
    else: #R อยู่ column เดียวกับ king
        dcol = 0 #ไม่ต้องขยับ column
        if row < king_row:
            drow = 1 #ขยับ row ไปทางข้างล่าง
        else:
            drow = -1 #ขยับ row ไปทางข้างบน

    return is_path_clear(board, row, col, king_row, king_col, drow, dcol)

def bishop_moves(board, row, col, king_row, king_col): #ตาเดินของ Bishop
    row_distance = king_row - row
    col_distance = king_col - col
    #หาตัว B กับ K ว่าอยู่ห่างกันกี่ row และกี่ column

    if row_distance == 0:
        return False #B อยู่ในแถวเดียวกับ K

    if abs(row_distance) != abs(col_distance): #ระยะห่างแถวกับระยะห่างคอลัมน์ต้องเท่ากัน
        return False

    if row_distance > 0:
        drow = 1 #เดินลง
    else:
        drow = -1 #เดินขึ้น

    if col_distance > 0:
        dcol = 1#เดินขวา
    else:
        dcol = -1 #เดินซ้าย

    return is_path_clear(board, row, col, king_row, king_col, drow, dcol)


def queen_moves(board, row, col, king_row, king_col):

    if rook_moves(board, row, col, king_row, king_col):
        return True

    if bishop_moves(board, row, col, king_row, king_col):
        return True

    return False
    #เรียกใช้ทั้ง rook_moves และ bishop_moves

def pawn_moves(row, col, king_row, king_col):

    if king_row == row - 1: #ตรวจสอบว่า king อยู่แถวบนของ pawn หรือไม่
        if king_col == col - 1 or king_col == col + 1: #ตรวจสอบว่า king อยู่ทางซ้ายหรือขวาของ pawn หรือไม่
            return True

    return False


def checkmate(board_text):

    board = parse_board(board_text) #แปลงเป็นตาราง
    if board is None: #กระดานผิดรูป
        return

    king_row, king_col = find_king(board) #หา king
    if king_row == -1: #มี king มากกว่า 1 ตัว
        return

    for row in range(len(board)): #หาตำแหน่งตัวหมากในแถว
        for col in range(len(board[row])): #หาตำแหน่งตัวหมากในคอลัมน์
            piece = board[row][col] #หาตำแหน่งของตัวหมากแต่ละตัว

            if row == king_row and col == king_col: #ข้ามการตรวจสอบตัวหมากที่เป็น king
                continue

            if piece == 'R': #R Checkmate K
                if rook_moves(board, row, col, king_row, king_col):
                    print("Success")
                    return

            if piece == 'B': #B Checkmate K
                if bishop_moves(board, row, col, king_row, king_col):
                    print("Success")
                    return

            if piece == 'Q': #Q Checkmate K
                if queen_moves(board, row, col, king_row, king_col):
                    print("Success")
                    return

            if piece == 'P': #P Checkmate K
                if pawn_moves(row, col, king_row, king_col):
                    print("Success")
                    return

    print("Fail")