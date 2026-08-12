import math


def transform(grid):
    fixed_cells = [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 4
    ]
    center_row = sum(row for row, _ in fixed_cells) / len(fixed_cells)
    center_col = sum(col for _, col in fixed_cells) / len(fixed_cells)
    moving_colors = sorted({value for row in grid for value in row} - {4, 7})

    def angle(color):
        cells = [
            (row, col)
            for row in range(len(grid))
            for col in range(len(grid[0]))
            if grid[row][col] == color
        ]
        row = sum(r for r, _ in cells) / len(cells)
        col = sum(c for _, c in cells) / len(cells)
        return math.atan2(row - center_row, col - center_col)

    clockwise = sorted(moving_colors, key=angle)
    replacement = {
        color: clockwise[(index - 1) % len(clockwise)]
        for index, color in enumerate(clockwise)
    }
    return [[replacement.get(value, value) for value in row] for row in grid]
