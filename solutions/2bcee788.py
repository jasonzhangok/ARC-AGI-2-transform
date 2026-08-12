def transform(grid):
    height, width = (len(grid), len(grid[0]))
    counts = {}
    for cell_value in (value for row in grid for value in row if value not in (0, 2)):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    main = max(counts, key=counts.get)
    main_cells = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == main}
    marker_cells = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2}
    adjacent = [(mr, mc, rr, cc) for mr, mc in marker_cells for rr, cc in main_cells if abs(mr - rr) + abs(mc - cc) == 1]
    mr, mc, rr, cc = adjacent[0]
    horizontal_axis = mr != rr
    doubled_axis = mr + rr if horizontal_axis else mc + cc
    result = [[3] * width for _ in range(height)]
    for r, c in main_cells:
        result[r][c] = main
        if horizontal_axis:
            result[doubled_axis - r][c] = main
        else:
            result[r][doubled_axis - c] = main
    output = result
    return output
