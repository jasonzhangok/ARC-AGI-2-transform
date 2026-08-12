def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    output = [[0 for _ in range(width)] for _ in range(height)]
    colors = []
    for row in grid:
        for value in row:
            if value != 0 and value not in colors:
                colors.append(value)

    for color in colors:
        rows = []
        columns = []
        for r in range(height):
            for c in range(width):
                if grid[r][c] == color:
                    rows.append(r)
                    if c not in columns:
                        columns.append(c)
        if not rows or len(columns) != 2:
            continue
        columns.sort()
        top = min(rows)
        bottom = max(rows)
        segment_length = bottom - top + 1

        for r in range(height):
            if r < top:
                offset = (top - r + segment_length - 1) // segment_length
            elif r > bottom:
                offset = (r - bottom + segment_length - 1) // segment_length
            else:
                offset = 0
            positions = (columns[0] - offset, columns[1] + offset)
            for c in positions:
                if 0 <= c < width:
                    if output[r][c] == 0 or output[r][c] == color:
                        output[r][c] = color
                    else:
                        output[r][c] = 6

    return output
