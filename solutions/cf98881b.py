def transform(grid):
    separators = [c for c in range(len(grid[0])) if all(row[c] == 2 for row in grid)]
    bounds = [-1] + separators + [len(grid[0])]
    panels = [[row[bounds[i] + 1:bounds[i + 1]] for row in grid] for i in range(3)]
    output = [
        [next((panel[r][c] for panel in panels if panel[r][c] != 0), 0) for c in range(4)]
        for r in range(4)
    ]
    return output
