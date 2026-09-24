def attackers(board):
    if not isinstance(board, str):
        return None

    rows = board.splitlines()
    size = len(rows)
    if size == 0 or any(len(row) != size for row in rows):
        return None

    kings = [
        (row, col)
        for row in range(size)
        for col in range(size)
        if rows[row][col] == "K"
    ]
    if len(kings) != 1:
        return None

    king_row, king_col = kings[0]
    found = []

    pawn_row = king_row + 1
    if pawn_row < size:
        for pawn_col in (king_col - 1, king_col + 1):
            if 0 <= pawn_col < size and rows[pawn_row][pawn_col] == "P":
                found.append(("P", pawn_row + 1, pawn_col + 1))

    directions = (
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1),
    )
    for row_step, col_step in directions:
        row = king_row + row_step
        col = king_col + col_step
        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]
            straight = row_step == 0 or col_step == 0
            if piece == "Q" or (straight and piece == "R") or (
                not straight and piece == "B"
            ):
                found.append((piece, row + 1, col + 1))
            if piece in "KPRBQ":
                break
            row += row_step
            col += col_step

    return found


def checkmate(board, explain=False):
    found = attackers(board)
    if found is None:
        print("Error")
    elif found:
        print("Success")
        if explain:
            for piece, row, col in found:
                print(f"Attacker: {piece} at row {row}, column {col}")
    else:
        print("Fail")
