def transform(grid):
    h, w = len(grid), len(grid[0])
    cross_row = next(r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] != 0)
    color = grid[cross_row][0]
    cross_col = next(c for c in range(w) if all(grid[r][c] == color for r in range(h)))
    source = [[grid[r][c] != 0 for c in range(cross_col)] for r in range(cross_row)]
    top = []
    for row in source:
        values = [color if v else 0 for v in row]
        top.append(values + values[::-1])
    output = top + [row[:] for row in top[::-1]]
    return output
