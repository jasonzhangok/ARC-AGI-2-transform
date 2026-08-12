def transform(grid):
    output = [row[:] for row in grid]
    fill_by_side = {5: 8, 7: 4, 9: 3}

    _grid = grid
    height, width = len(_grid), len(_grid[0])
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if _grid[r][c] == 0 or (r, c) in seen:
                continue
            color = _grid[r][c]
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
                        and _grid[yy][xx] == color
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append((color, points))
    _components_result_1 = result
    for color, points in _components_result_1:
        rows = [r for r, _ in points]
        cols = [c for _, c in points]
        top, bottom = min(rows), max(rows)
        left, right = min(cols), max(cols)
        side = bottom - top + 1

        if (
            color == 2
            and side >= 3
            and side == right - left + 1
            and len(points) == 4 * (side - 1)
        ):
            fill = fill_by_side[side]
            for r in range(top + 1, bottom):
                for c in range(left + 1, right):
                    if output[r][c] == 0:
                        output[r][c] = fill

    return output
