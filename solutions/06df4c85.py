

def transform(grid):
    output = [row[:] for row in grid]
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    lattice_color = max(counts, key=counts.get)

    for color in counts:
        if color == lattice_color:
            continue
        blocks = []
        _grid = grid
        _color = color
        height, width = len(_grid), len(_grid[0])
        seen = set()
        result = []
        for r in range(height):
            for c in range(width):
                if _grid[r][c] != _color or (r, c) in seen:
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
                            and _grid[yy][xx] == _color
                        ):
                            seen.add((yy, xx))
                            stack.append((yy, xx))
                result.append(points)
        _components_result_1 = result
        for points in _components_result_1:
            top = min(r for r, _ in points)
            left = min(c for _, c in points)
            bottom = max(r for r, _ in points)
            right = max(c for _, c in points)
            if bottom - top == 1 and right - left == 1 and len(points) == 4:
                blocks.append((top, left))

        by_row = {}
        by_column = {}
        for top, left in blocks:
            by_row.setdefault(top, []).append(left)
            by_column.setdefault(left, []).append(top)

        for top, columns in by_row.items():
            if len(columns) >= 2:
                for left in range(min(columns), max(columns) + 1, 3):
                    for dr in (0, 1):
                        for dc in (0, 1):
                            output[top + dr][left + dc] = color
        for left, rows in by_column.items():
            if len(rows) >= 2:
                for top in range(min(rows), max(rows) + 1, 3):
                    for dr in (0, 1):
                        for dc in (0, 1):
                            output[top + dr][left + dc] = color

    return output
