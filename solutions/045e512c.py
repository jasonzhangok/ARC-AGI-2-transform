

def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    template_color = max(counts, key=counts.get)
    template = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == template_color
    ]
    top, bottom = min(r for r, _ in template), max(r for r, _ in template)
    left, right = min(c for _, c in template), max(c for _, c in template)
    block_height, block_width = bottom - top + 1, right - left + 1

    for color in counts:
        if color == template_color:
            continue
        _grid = grid
        _color = color
        height, width = len(_grid), len(_grid[0])
        directions = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        )
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
                    for dy, dx in directions:
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
        for marker in _components_result_1:
            center_r = sum(r for r, _ in marker) / len(marker)
            center_c = sum(c for _, c in marker) / len(marker)
            dr = -(block_height + 1) if center_r < top else (
                block_height + 1 if center_r > bottom else 0
            )
            dc = -(block_width + 1) if center_c < left else (
                block_width + 1 if center_c > right else 0
            )

            multiple = 1
            while True:
                stamp = [
                    (r + multiple * dr, c + multiple * dc)
                    for r, c in template
                    if 0 <= r + multiple * dr < height
                    and 0 <= c + multiple * dc < width
                ]
                if not stamp:
                    break
                for r, c in stamp:
                    output[r][c] = color
                multiple += 1

    return output
