

def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    ink = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        ink[cell_value] = ink.get(cell_value, 0) + 1
    ink = max(ink, key=ink.get)
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != ink or (r, c) in seen:
                continue
            queue = list([(r, c)])
            seen.add((r, c))
            component = []
            while queue:
                x, y = queue.pop(0)
                component.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == ink and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            r0, r1 = min(x for x, _ in component), max(x for x, _ in component)
            c0, c1 = min(y for _, y in component), max(y for _, y in component)
            if r1 - r0 < 2 or c1 - c0 < 2:
                continue
            border = ({(r0, y) for y in range(c0, c1 + 1)} |
                      {(r1, y) for y in range(c0, c1 + 1)} |
                      {(x, c0) for x in range(r0, r1 + 1)} |
                      {(x, c1) for x in range(r0, r1 + 1)})
            if all(grid[x][y] == ink for x, y in border):
                side = min(r1 - r0 - 1, c1 - c0 - 1)
                fill = 7 if side % 2 else 2
                for x in range(r0 + 1, r1):
                    for y in range(c0 + 1, c1):
                        if grid[x][y] == 0:
                            output[x][y] = fill
    return output
