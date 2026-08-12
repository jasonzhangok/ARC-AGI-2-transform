def transform(grid):
    height, width = len(grid), len(grid[0])
    frequencies = {}
    for row in grid:
        for value in row:
            frequencies[value] = frequencies.get(value, 0) + 1
    background = None
    for value in frequencies:
        if background is None or frequencies[value] > frequencies[background]:
            background = value
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    component_counts = {}
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        queue = [start]
        position = 0
        while position < len(queue):
            r, c = queue[position]
            position += 1
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    queue.append(point)
        component_counts[color] = component_counts.get(color, 0) + 1
    ordered = [record[2] for record in sorted((-pair[1], pair[0], pair) for pair in component_counts.items())]
    size = max(component_counts.values())
    output = [[background] * (size - count) + [color] * count for color, count in ordered]
    return output
