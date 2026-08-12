def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set(value for row in grid for value in row) - {0, 8}
    counts = {
        color: sum(value == color for row in grid for value in row)
        for color in colors
    }
    center_color = min(colors, key=counts.get)
    alternating_color = next(color for color in colors if color != center_color)
    center = next(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == center_color
    )

    output = [row[:] for row in grid]
    distances = {center: 0}
    pending = [center]
    while pending:
        row, col = pending.pop(0)
        for neighbor in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            nr, nc = neighbor
            if (
                0 <= nr < height
                and 0 <= nc < width
                and grid[nr][nc] != 8
                and neighbor not in distances
            ):
                distances[neighbor] = distances[row, col] + 1
                pending.append(neighbor)

    for (row, col), distance in distances.items():
        output[row][col] = center_color if distance % 2 == 0 else alternating_color
    return output
