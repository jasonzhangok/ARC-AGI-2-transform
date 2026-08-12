

def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    counts = {}
    for cell_value in (value for row in grid for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    background = max(counts, key=counts.get)
    singleton_colors = {color for color, count in counts.items() if count == 1}
    boundaries = []

    _grid = grid
    _background = background
    height, width = len(_grid), len(_grid[0])
    directions = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr, dc) != (0, 0)
    ]
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if _grid[r][c] == _background or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            points = []
            while stack:
                y, x = stack.pop()
                points.append((y, x))
                for dy, dx in directions:
                    yy, xx = y + dy, x + dx
                    if (
                        0 <= yy < height
                        and 0 <= xx < width
                        and (yy, xx) not in seen
                        and _grid[yy][xx] != _background
                    ):
                        seen.add((yy, xx))
                        stack.append((yy, xx))
            result.append(points)
    _components_result_1 = result
    for component in _components_result_1:
        signal = next(
            (point for point in component if grid[point[0]][point[1]] in singleton_colors),
            None,
        )
        if signal is None:
            continue
        signal_r, signal_c = signal
        signal_color = grid[signal_r][signal_c]
        other = [point for point in component if point != signal]
        center_r = sum(r for r, _ in other) / len(other)
        center_c = sum(c for _, c in other) / len(other)
        vertical = abs(signal_r - center_r) > abs(signal_c - center_c)
        top, bottom = min(r for r, _ in component), max(r for r, _ in component)
        left, right = min(c for _, c in component), max(c for _, c in component)

        if vertical:
            direction = -1 if signal_r < center_r else 1
            step = bottom - top + 1
            r = signal_r + direction * step
            while 0 <= r < height:
                output[r][signal_c] = signal_color
                r += direction * step
            boundary = 0 if direction == -1 else height - 1
            output[boundary] = [signal_color] * width
            boundaries.append(("row", boundary))
        else:
            direction = -1 if signal_c < center_c else 1
            step = right - left + 1
            c = signal_c + direction * step
            while 0 <= c < width:
                output[signal_r][c] = signal_color
                c += direction * step
            boundary = 0 if direction == -1 else width - 1
            for r in range(height):
                output[r][boundary] = signal_color
            boundaries.append(("column", boundary))

    rows = [value for kind, value in boundaries if kind == "row"]
    columns = [value for kind, value in boundaries if kind == "column"]
    for r in rows:
        for c in columns:
            output[r][c] = 0
    return output
