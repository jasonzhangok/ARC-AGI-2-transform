def transform(grid):
    output = [row[:] for row in grid]
    legend = [(c, value) for c, value in enumerate(grid[0]) if value != 0]
    seen = set()
    for r in range(2, len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            stack, cells = ([(r, c)], [])
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] == 5) and ((nx, ny) not in seen):
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            center = sum((y for _, y in cells)) / len(cells)
            _, color = min(((abs(_key_item_1[0] - center), _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(legend)))[2]
            for x, y in cells:
                output[x][y] = color
    return output
