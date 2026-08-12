def transform(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0 or (r, c) in seen:
                continue
            cells = []
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] != 0
                            and (ny, nx) not in seen):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            components.append(cells)
    main = max(components, key=len)
    main_colors = {grid[r][c] for r, c in main}
    mapping = {}
    for cells in components:
        if cells is main:
            continue
        colors = {grid[r][c] for r, c in cells}
        if len(cells) == 2 and len(colors) == 2:
            source = next((v for v in colors if v in main_colors), None)
            if source is not None:
                mapping[source] = next(v for v in colors if v != source)
    r0, r1 = min(r for r, _ in main), max(r for r, _ in main)
    c0, c1 = min(c for _, c in main), max(c for _, c in main)
    output = [[mapping.get(grid[r][c], grid[r][c]) for c in range(c0, c1 + 1)]
            for r in range(r0, r1 + 1)]
    return output
