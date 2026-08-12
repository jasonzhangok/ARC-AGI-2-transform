def transform(grid):
    h, w = (len(grid), len(grid[0]))
    seen, crops = (set(), [])
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            stack, cells = ([(r, c)], [])
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < h and 0 <= ny < w and (grid[nx][ny] != 0) and ((nx, ny) not in seen):
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            r0, r1 = (min((x for x, _ in cells)), max((x for x, _ in cells)))
            c0, c1 = (min((y for _, y in cells)), max((y for _, y in cells)))
            crop = tuple((tuple((grid[x][y] for y in range(c0, c1 + 1))) for x in range(r0, r1 + 1)))
            crops.append(crop)
    counts = {}
    for cell_value in crops:
        counts[cell_value] = counts.get(cell_value, 0) + 1
    unique = next((crop for crop in crops if counts[crop] == 1))
    output = [list(row) for row in unique]
    return output
