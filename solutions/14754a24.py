def transform(grid):
    h, w = (len(grid), len(grid[0]))
    candidates = []
    for r in range(h):
        for c in range(w):
            cells = {(r, c)}
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = (r + dr, c + dc)
                if 0 <= nr < h and 0 <= nc < w:
                    cells.add((nr, nc))
            values = [grid[y][x] for y, x in cells]
            count = values.count(4)
            if count >= 2 and all((value in (4, 5) for value in values)):
                candidates.append((count, r, c, cells))
    out = [row[:] for row in grid]
    used = set()
    for _, _, _, cells in [_sort_record_1[2] for _sort_record_1 in sorted(((-_sort_item_1[0], _sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(candidates)))]:
        if cells & used:
            continue
        used.update(cells)
        for r, c in cells:
            if grid[r][c] == 5:
                out[r][c] = 2
    output = out
    return output
