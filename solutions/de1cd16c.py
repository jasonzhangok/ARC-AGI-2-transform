def transform(grid):
    frequencies = {}
    for row in grid:
        for value in row:
            frequencies[value] = frequencies.get(value, 0) + 1
    marker = None
    for value in frequencies:
        if marker is None or frequencies[value] < frequencies[marker]:
            marker = value
    region_counts = {}
    h, w = len(grid), len(grid[0])
    for r in range(h):
        for c in range(w):
            if grid[r][c] != marker:
                continue
            neighbors = {}
            for x in range(max(0, r - 1), min(h, r + 2)):
                for y in range(max(0, c - 1), min(w, c + 2)):
                    value = grid[x][y]
                    if value != marker:
                        neighbors[value] = neighbors.get(value, 0) + 1
            if neighbors:
                neighbor_color = None
                for value in neighbors:
                    if neighbor_color is None or neighbors[value] > neighbors[neighbor_color]:
                        neighbor_color = value
                region_counts[neighbor_color] = region_counts.get(neighbor_color, 0) + 1
    result_color = None
    for value in region_counts:
        if result_color is None or region_counts[value] > region_counts[result_color]:
            result_color = value
    output = [[result_color]]
    return output
