def transform(grid):
    height = len(grid)
    width = len(grid[0])

    nonempty_rows = []
    nonempty_cols = []
    for row in range(height):
        if any(grid[row][col] != 0 for col in range(width)):
            nonempty_rows.append(row)
    for col in range(width):
        if any(grid[row][col] != 0 for row in range(height)):
            nonempty_cols.append(col)

    top = min(nonempty_rows)
    bottom = max(nonempty_rows)
    left = min(nonempty_cols)
    right = max(nonempty_cols)

    row_groups = []
    start = top
    signature = {grid[top][col] for col in range(left, right + 1)
                 if grid[top][col] != 0}
    for row in range(top + 1, bottom + 1):
        current = {grid[row][col] for col in range(left, right + 1)
                   if grid[row][col] != 0}
        if current != signature:
            row_groups.append((start, row - 1))
            start = row
            signature = current
    row_groups.append((start, bottom))

    col_groups = []
    start = left
    signature = {grid[row][left] for row in range(top, bottom + 1)
                 if grid[row][left] != 0}
    for col in range(left + 1, right + 1):
        current = {grid[row][col] for row in range(top, bottom + 1)
                   if grid[row][col] != 0}
        if current != signature:
            col_groups.append((start, col - 1))
            start = col
            signature = current
    col_groups.append((start, right))

    output = []
    for row_start, row_end in row_groups:
        compressed = []
        for col_start, col_end in col_groups:
            counts = {}
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    color = grid[row][col]
                    if color != 0:
                        counts[color] = counts.get(color, 0) + 1
            compressed.append(max(counts, key=counts.get))
        output.append(compressed[::-1])

    return output
