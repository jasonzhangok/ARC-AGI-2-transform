from collections import Counter


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = Counter(value for row in grid for value in row)
    rare = min(counts, key=counts.get)
    adjacency = Counter()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != rare:
                continue
            for nr, nc in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= nr < height
                    and 0 <= nc < width
                    and grid[nr][nc] != rare
                ):
                    adjacency[grid[nr][nc]] += 1
    companion = adjacency.most_common(1)[0][0]
    target = {rare, companion}
    rows = [
        row
        for row in range(height)
        if any(grid[row][col] in target for col in range(width))
    ]
    cols = [
        col
        for col in range(width)
        if any(grid[row][col] in target for row in range(height))
    ]
    return [[grid[row][col] for col in cols] for row in rows]
