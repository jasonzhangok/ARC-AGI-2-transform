def transform(grid):
    result = [row[:] for row in grid]
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    main = max(counts, key=counts.get)
    marker = min(counts, key=counts.get)
    marker_cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == marker]
    r, c = marker_cells[0]
    body = [(rr, cc) for rr, row in enumerate(grid) for cc, value in enumerate(row) if value == main]
    dr_total = sum((rr - r for rr, _ in body))
    dc_total = sum((cc - c for _, cc in body))
    if abs(dr_total) >= abs(dc_total):
        dr, dc = (1 if dr_total > 0 else -1, 0)
    else:
        dr, dc = (0, 1 if dc_total > 0 else -1)
    r += dr
    c += dc
    while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if result[r][c] == 0:
            result[r][c] = marker
        r += dr
        c += dc
    output = result
    return output
