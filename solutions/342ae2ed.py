def transform(grid):
    height, width = (len(grid), len(grid[0]))
    background = 7
    colors = {value for row in grid for value in row if value != background}
    result = [row[:] for row in grid]
    for color in colors:
        remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
        components = []
        while remaining:
            start = remaining.pop()
            component = {start}
            queue = list([start])
            while queue:
                r, c = queue.pop(0)
                for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if point in remaining:
                        remaining.remove(point)
                        component.add(point)
                        queue.append(point)
            components.append(component)
        if len(components) != 2:
            continue
        first, second = components
        a, b = min(((max(abs(_item_1[0][0] - _item_1[1][0]), abs(_item_1[0][1] - _item_1[1][1])), _index_1, _item_1) for _index_1, _item_1 in enumerate(((p, q) for p in first for q in second))))[2]
        dr = (b[0] > a[0]) - (b[0] < a[0])
        dc = (b[1] > a[1]) - (b[1] < a[1])
        r, c = (a[0] + dr, a[1] + dc)
        while (r, c) != b:
            result[r][c] = color
            r += dr
            c += dc
    output = result
    return output
