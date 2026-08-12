def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    seen = set()
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 3 or (r, c) in seen:
                continue
            component = []
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                component.append((y, x))
                for dy, dx in directions:
                    ny, nx = (y + dy, x + dx)
                    if 0 <= ny < h and 0 <= nx < w and (grid[ny][nx] == 3) and ((ny, nx) not in seen):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            cells = set(component)
            sources = {(ny, nx) for y, x in component for dy, dx in directions for ny, nx in ((y + dy, x + dx),) if 0 <= ny < h and 0 <= nx < w and (grid[ny][nx] == 5)}
            if not sources:
                continue
            distance = {}
            queue = []
            for y, x in component:
                if any((abs(y - sy) + abs(x - sx) == 1 for sy, sx in sources)):
                    distance[y, x] = 1
                    queue.append((y, x))
            while queue:
                y, x = queue.pop(0)
                for dy, dx in directions:
                    neighbor = (y + dy, x + dx)
                    if neighbor in cells and neighbor not in distance:
                        distance[neighbor] = distance[y, x] + 1
                        queue.append(neighbor)
            farthest = max(((distance[_item_1], _index_1, _item_1) for _index_1, _item_1 in enumerate(component)))[2]
            next_cell = next((neighbor for dy, dx in directions for neighbor in ((farthest[0] + dy, farthest[1] + dx),) if neighbor in cells and distance[neighbor] == distance[farthest] - 1))
            for y, x in component:
                out[y][x] = 7
            for y, x in sources:
                out[y][x] = 7
            out[farthest[0]][farthest[1]] = 3
            out[next_cell[0]][next_cell[1]] = 5
    output = out
    return output
