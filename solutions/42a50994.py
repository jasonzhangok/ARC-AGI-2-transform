def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    for r in range(height):
        for c in range(width):
            color = grid[r][c]
            if color == 0:
                continue
            has_neighbor = any(
                0 <= r + dr < height
                and 0 <= c + dc < width
                and grid[r + dr][c + dc] == color
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if (dr, dc) != (0, 0)
            )
            if not has_neighbor:
                result[r][c] = 0
    output = result
    return output
