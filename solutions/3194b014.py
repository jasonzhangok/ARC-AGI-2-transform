def transform(grid):
    height, width = (len(grid), len(grid[0]))
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0}
    components = []
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        component = {start}
        queue = list([start])
        while queue:
            r, c = queue.pop(0)
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    component.add(point)
                    queue.append(point)
        components.append((color, component))
    color, _ = max(((len(_item_1[1]), _index_1, _item_1) for _index_1, _item_1 in enumerate(components)))[2]
    output = [[color] * 3 for _ in range(3)]
    return output
