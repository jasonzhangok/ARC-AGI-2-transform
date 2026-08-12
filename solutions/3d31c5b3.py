def transform(grid):
    panel_height = len(grid) // 4
    width = len(grid[0])
    result = [[0 for _ in range(width)] for _ in range(panel_height)]
    for panel in (0, 1, 3, 2):
        for r in range(panel_height):
            for c in range(width):
                if result[r][c] == 0 and grid[panel * panel_height + r][c] != 0:
                    result[r][c] = grid[panel * panel_height + r][c]
    output = result
    return output
