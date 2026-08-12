def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    points = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] != background:
                points.append((r, c))
    color = grid[points[0][0]][points[0][1]]
    center_r = sum(r for r, c in points) // len(points)
    center_c = sum(c for r, c in points) // len(points)
    spacing = min(max(abs(r - center_r), abs(c - center_c))
                  for r, c in points if (r, c) != (center_r, center_c))

    output = [row[:] for row in grid]
    for r in range(height):
        for c in range(width):
            distance = max(abs(r - center_r), abs(c - center_c))
            if distance % spacing == 0:
                output[r][c] = color
    return output
