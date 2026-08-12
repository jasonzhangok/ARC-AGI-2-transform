def transform(grid):
    height = len(grid)
    width = len(grid[0])
    corners = ((0, 0), (0, width - 2), (height - 2, 0), (height - 2, width - 2))
    best_row, best_col = corners[0]
    best_score = -1
    for row, col in corners:
        score = abs(grid[row][col] + grid[row + 1][col + 1]
                    - grid[row][col + 1] - grid[row + 1][col])
        if score > best_score:
            best_score = score
            best_row, best_col = row, col
    output = [grid[best_row][best_col:best_col + 2],
            grid[best_row + 1][best_col:best_col + 2]]
    return output
