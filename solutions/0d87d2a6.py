def _red_components(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] != 2 or (r, c) in seen:
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
                        and grid[yy][xx] == 2
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append(points)
    return result


def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    blue = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 1
    ]
    line_points = set()
    for i, first in enumerate(blue):
        for second in blue[i + 1 :]:
            if first[0] == second[0]:
                line_points.update((first[0], c) for c in range(min(first[1], second[1]), max(first[1], second[1]) + 1))
            if first[1] == second[1]:
                line_points.update((r, first[1]) for r in range(min(first[0], second[0]), max(first[0], second[0]) + 1))

    for component in _red_components(grid):
        if any(point in line_points for point in component):
            for r, c in component:
                output[r][c] = 1
    for r, c in line_points:
        output[r][c] = 1
    return output
