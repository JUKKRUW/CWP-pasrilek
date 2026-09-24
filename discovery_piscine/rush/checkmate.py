def checkmate(board):
    if not isinstance(board, str):
        print("Error")
        return

    rows = board.splitlines()
    size = len(rows)

    if size == 0 or any(len(row) != size for row in rows):
        print("Error")
        return

    kings = [
        (r, c)
        for r in range(size)
        for c in range(size)
        if rows[r][c] == "K"
    ]
    print(kings)
    if len(kings) != 1:
        print("Error")
        return

    king_row, king_col = kings[0]

    pawn_row = king_row + 1
    if pawn_row < size:
        for pawn_col in (king_col - 1, king_col + 1):
            if 0 <= pawn_col < size and rows[pawn_row][pawn_col] == "P":
                print("Success")
                return

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1),
    ]

    for row_step, col_step in directions:
        r = king_row + row_step
        c = king_col + col_step

        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]

            if piece == "Q":
                print("Success")
                return
            if row_step == 0 or col_step == 0:
                if piece == "R":
                    print("Success")
                    return
            else:
                if piece == "B":
                    print("Success")
                    return

            if piece in "KPRBQ":
                break

            r += row_step
            c += col_step

    print("Fail")