from collections import Counter, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    path_color = next(value for row in grid for value in row if value != background)
    exterior = set()
    queue = deque()
    for row in range(height):
        for col in range(width):
            if (row in (0, height - 1) or col in (0, width - 1)) and grid[row][col] == background:
                exterior.add((row, col))
                queue.append((row, col))
    while queue:
        row, col = queue.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            y, x = row + dr, col + dc
            if (0 <= y < height and 0 <= x < width and
                    grid[y][x] == background and (y, x) not in exterior):
                exterior.add((y, x))
                queue.append((y, x))

    output = [row[:] for row in grid]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for row in range(height):
        for col in range(width):
            if grid[row][col] != path_color:
                continue
            neighbors = [
                (dr, dc)
                for dr, dc in directions
                if 0 <= row + dr < height and 0 <= col + dc < width
                and grid[row + dr][col + dc] == path_color
            ]
            if len(neighbors) != 2:
                continue
            (dr1, dc1), (dr2, dc2) = neighbors
            if dr1 * dr2 + dc1 * dc2 != 0:
                continue
            diagonal = (row + dr1 + dr2, col + dc1 + dc2)
            output[row][col] = 2 if diagonal in exterior else 4
    return output
