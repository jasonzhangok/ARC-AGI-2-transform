from collections import Counter, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    special_points = [
        (r, c, grid[r][c])
        for r in range(height)
        for c in range(width)
        if grid[r][c] not in (background, 1)
    ]
    templates = {}
    template_anchors = set()
    for row, col, color in special_points:
        adjacent_ones = any(
            0 <= row + dr < height and 0 <= col + dc < width and grid[row + dr][col + dc] == 1
            for dr in (-1, 0, 1)
            for dc in (-1, 0, 1)
            if dr or dc
        )
        if not adjacent_ones:
            continue
        allowed = {1, color}
        queue = deque([(row, col)])
        seen = {(row, col)}
        while queue:
            y, x = queue.popleft()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if not (dy or dx):
                        continue
                    point = (y + dy, x + dx)
                    if (0 <= point[0] < height and 0 <= point[1] < width and point not in seen
                            and grid[point[0]][point[1]] in allowed):
                        seen.add(point)
                        queue.append(point)
        offsets = {(y - row, x - col) for y, x in seen if grid[y][x] == 1}
        if offsets:
            templates[color] = offsets
            template_anchors.add((row, col))

    output = [[background] * width for _ in range(height)]
    for row, col, color in special_points:
        if color not in templates or (row, col) in template_anchors:
            continue
        output[row][col] = color
        for dr, dc in templates[color]:
            y, x = row + dr, col + dc
            if 0 <= y < height and 0 <= x < width:
                output[y][x] = 1
    return output
