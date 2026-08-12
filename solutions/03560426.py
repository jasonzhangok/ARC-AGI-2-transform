def _components(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            color = grid[r][c]
            stack = [(r, c)]
            seen.add((r, c))
            points = []
            while stack:
                y, x = stack.pop()
                points.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    yy, xx = y + dy, x + dx
                    if (
                        0 <= yy < height
                        and 0 <= xx < width
                        and (yy, xx) not in seen
                        and grid[yy][xx] == color
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append((color, points))
    return result


def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [[0] * width for _ in range(height)]
    objects = []

    for color, points in _components(grid):
        top = min(r for r, _ in points)
        bottom = max(r for r, _ in points)
        left = min(c for _, c in points)
        right = max(c for _, c in points)
        relative = [(r - top, c - left) for r, c in points]
        objects.append((left, color, relative, bottom - top + 1, right - left + 1))

    objects.sort()
    previous = None
    for _, color, points, object_height, object_width in objects:
        if previous is None:
            top = left = 0
        else:
            old_top, old_left, old_height, old_width = previous
            top = old_top + old_height - 1
            left = old_left + old_width - 1
        for r, c in points:
            if 0 <= top + r < height and 0 <= left + c < width:
                output[top + r][left + c] = color
        previous = (top, left, object_height, object_width)

    return output
