def transform(grid):
    height, width = len(grid), len(grid[0])
    points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2]
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    output = [[0] * width for _ in range(height)]
    for row in range(height):
        for col in range(width):
            if row in (top, bottom) or col in (left, right):
                output[row][col] = 2
            elif top < row < bottom and left < col < right:
                output[row][col] = 1
    return output
