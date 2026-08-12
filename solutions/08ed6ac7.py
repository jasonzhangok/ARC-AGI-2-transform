def transform(grid):
    height, width = len(grid), len(grid[0])
    bars = []
    for c in range(width):
        points = [(r, c) for r in range(height) if grid[r][c] == 5]
        if points:
            bars.append(points)
    bars.sort(key=len, reverse=True)

    output = [[0] * width for _ in range(height)]
    for rank, points in enumerate(bars, start=1):
        for r, c in points:
            output[r][c] = rank
    return output
