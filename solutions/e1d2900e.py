def transform(grid):
    height = len(grid)
    width = len(grid[0])
    blocks = []
    for row in range(height - 1):
        for col in range(width - 1):
            if (
                grid[row][col] == 2
                and grid[row][col + 1] == 2
                and grid[row + 1][col] == 2
                and grid[row + 1][col + 1] == 2
                and (row == 0 or grid[row - 1][col] != 2)
                and (col == 0 or grid[row][col - 1] != 2)
            ):
                blocks.append((row, col))

    result = [line[:] for line in grid]
    moves = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1:
                continue
            best_distance = height + width
            target_row = -1
            target_col = -1
            for block_row, block_col in blocks:
                row_gap = max(block_row - row, row - block_row - 1, 0)
                col_gap = max(block_col - col, col - block_col - 1, 0)
                distance = max(row_gap, col_gap)
                if distance < best_distance:
                    best_distance = distance
                    target_row = block_row
                    target_col = block_col

            new_row = row
            new_col = col
            if target_row <= row <= target_row + 1:
                if col < target_col:
                    new_col = target_col - 1
                elif col > target_col + 1:
                    new_col = target_col + 2
            elif target_col <= col <= target_col + 1:
                if row < target_row:
                    new_row = target_row - 1
                elif row > target_row + 1:
                    new_row = target_row + 2
            if (new_row, new_col) != (row, col):
                moves.append((row, col, new_row, new_col))

    for row, col, new_row, new_col in moves:
        result[row][col] = 0
    for row, col, new_row, new_col in moves:
        result[new_row][new_col] = 1
    return result
