from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    marker = next(color for color in counts if color not in (0, 4, 5))

    brush_center = next(
        (r, c)
        for r in range(1, height - 1)
        for c in range(1, width - 1)
        if grid[r][c] == marker
        and sum(
            grid[r + dr][c + dc] == 4
            for dr in (-1, 0, 1)
            for dc in (-1, 0, 1)
            if (dr, dc) != (0, 0)
        )
        >= 4
    )
    instruction_start = next(
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] == marker and (r, c) != brush_center
    )
    instruction_end = next(
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] == 4
        and max(abs(r - brush_center[0]), abs(c - brush_center[1])) > 1
    )

    center_row = brush_center[0] + instruction_end[0] - instruction_start[0]
    center_column = brush_center[1] + instruction_end[1] - instruction_start[1]
    result = [[marker for _ in range(width)] for _ in range(height)]

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (dr, dc) != (0, 0):
                result[center_row + dr][center_column + dc] = 4
    for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        r, c = center_row + dr, center_column + dc
        while 0 <= r < height and 0 <= c < width:
            result[r][c] = 4
            r += dr
            c += dc
    return result
