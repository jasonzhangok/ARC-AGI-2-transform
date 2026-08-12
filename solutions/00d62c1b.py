from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    exterior = set()
    queue = deque()

    for r in range(height):
        for c in (0, width - 1):
            if grid[r][c] == 0 and (r, c) not in exterior:
                exterior.add((r, c))
                queue.append((r, c))
    for c in range(width):
        for r in (0, height - 1):
            if grid[r][c] == 0 and (r, c) not in exterior:
                exterior.add((r, c))
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if (
                0 <= rr < height
                and 0 <= cc < width
                and grid[rr][cc] == 0
                and (rr, cc) not in exterior
            ):
                exterior.add((rr, cc))
                queue.append((rr, cc))

    return [
        [4 if value == 0 and (r, c) not in exterior else value for c, value in enumerate(row)]
        for r, row in enumerate(grid)
    ]
