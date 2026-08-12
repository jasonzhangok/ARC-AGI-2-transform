def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    output = [[0 for _ in range(width)] for _ in range(height)]
    seen = [[False for _ in range(width)] for _ in range(height)]

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or seen[start_row][start_col]:
                continue

            stack = [(start_row, start_col)]
            seen[start_row][start_col] = True
            object_cells = []
            while stack:
                row, col = stack.pop()
                object_cells.append((row, col))
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and grid[next_row][next_col] != 0
                        and not seen[next_row][next_col]
                    ):
                        seen[next_row][next_col] = True
                        stack.append((next_row, next_col))

            remaining_nines = {
                (row, col)
                for row, col in object_cells
                if grid[row][col] == 9
            }
            pieces = []
            while remaining_nines:
                first = remaining_nines.pop()
                stack = [first]
                piece = []
                while stack:
                    row, col = stack.pop()
                    piece.append((row, col))
                    for neighbor in (
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    ):
                        if neighbor in remaining_nines:
                            remaining_nines.remove(neighbor)
                            stack.append(neighbor)
                pieces.append(piece)

            if len(pieces) != 2:
                for piece in pieces:
                    for row, col in piece:
                        output[row][col] = 9
                continue

            first_size = len(pieces[0])
            second_size = len(pieces[1])
            first_row_sum = sum(row for row, col in pieces[0])
            first_col_sum = sum(col for row, col in pieces[0])
            second_row_sum = sum(row for row, col in pieces[1])
            second_col_sum = sum(col for row, col in pieces[1])
            row_separation = abs(
                first_row_sum * second_size - second_row_sum * first_size
            )
            col_separation = abs(
                first_col_sum * second_size - second_col_sum * first_size
            )

            for index in range(2):
                other = 1 - index
                piece_size = len(pieces[index])
                other_size = len(pieces[other])
                piece_row_sum = sum(row for row, col in pieces[index])
                piece_col_sum = sum(col for row, col in pieces[index])
                other_row_sum = sum(row for row, col in pieces[other])
                other_col_sum = sum(col for row, col in pieces[other])
                row_shift = 0
                col_shift = 0
                if row_separation > col_separation:
                    if piece_row_sum * other_size < other_row_sum * piece_size:
                        row_shift = -1
                    else:
                        row_shift = 1
                else:
                    if piece_col_sum * other_size < other_col_sum * piece_size:
                        col_shift = -1
                    else:
                        col_shift = 1

                for row, col in pieces[index]:
                    moved_row = row + row_shift
                    moved_col = col + col_shift
                    if 0 <= moved_row < height and 0 <= moved_col < width:
                        output[moved_row][moved_col] = 9

    return output
