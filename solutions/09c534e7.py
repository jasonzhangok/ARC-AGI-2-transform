def _components(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
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
                        and grid[yy][xx] != 0
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append(points)
    return result


def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for points in _components(grid):
        color = next(grid[r][c] for r, c in points if grid[r][c] != 1)
        for r, c in points:
            if all(
                0 <= r + dr < height
                and 0 <= c + dc < width
                and grid[r + dr][c + dc] != 0
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
            ):
                output[r][c] = color
    return output
