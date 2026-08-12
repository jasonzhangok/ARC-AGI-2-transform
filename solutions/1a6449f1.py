def transform(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value != 0}
    rectangles = []
    for color in colors:
        rows = sorted({r for r in range(height) for c in range(width) if grid[r][c] == color})
        cols = sorted({c for r in range(height) for c in range(width) if grid[r][c] == color})
        for top_index, top in enumerate(rows):
            for bottom in rows[top_index + 2:]:
                for left_index, left in enumerate(cols):
                    for right in cols[left_index + 2:]:
                        border = (
                            all(grid[top][c] == color and grid[bottom][c] == color for c in range(left, right + 1))
                            and all(grid[r][left] == color and grid[r][right] == color for r in range(top, bottom + 1))
                        )
                        if border:
                            rectangles.append(((bottom - top - 1) * (right - left - 1), top, bottom, left, right))
    _, top, bottom, left, right = max(rectangles)
    return [row[left + 1:right] for row in grid[top + 1:bottom]]
