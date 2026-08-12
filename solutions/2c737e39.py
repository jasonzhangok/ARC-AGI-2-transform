from collections import deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    nonzero = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0}
    marker_cells = {(r, c) for r, c in nonzero if grid[r][c] == 5}
    source_marker = next(
        (r, c)
        for r, c in marker_cells
        if any((rr, cc) in nonzero and grid[rr][cc] != 5 for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)))
    )
    target_marker = next(point for point in marker_cells if point != source_marker)
    component = {source_marker}
    queue = deque([source_marker])
    seen = {source_marker}
    while queue:
        r, c = queue.popleft()
        for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if point in nonzero and point not in seen and point != target_marker:
                seen.add(point)
                component.add(point)
                queue.append(point)
    dr = target_marker[0] - source_marker[0]
    dc = target_marker[1] - source_marker[1]
    result = [row[:] for row in grid]
    result[target_marker[0]][target_marker[1]] = 0
    for r, c in component:
        if grid[r][c] != 5:
            result[r + dr][c + dc] = grid[r][c]
    return result
