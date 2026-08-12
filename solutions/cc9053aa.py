def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    hazards = []
    endpoints = []
    route_cells = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 7:
                hazards.append((row, col))
            elif grid[row][col] == 8 or grid[row][col] == 9:
                route_cells.add((row, col))
                if grid[row][col] == 9:
                    endpoints.append((row, col))

    clearance = {}
    for row, col in route_cells:
        nearest = height + width
        for hazard_row, hazard_col in hazards:
            distance = abs(row - hazard_row) + abs(col - hazard_col)
            if distance < nearest:
                nearest = distance
        clearance[(row, col)] = nearest

    thresholds = sorted(set(clearance.values()), reverse=True)
    found = False
    for threshold in thresholds:
        if clearance[endpoints[0]] < threshold or clearance[endpoints[1]] < threshold:
            continue
        queue = [endpoints[0]]
        previous = {endpoints[0]: None}
        position = 0
        while position < len(queue):
            row, col = queue[position]
            position += 1
            if (row, col) == endpoints[1]:
                break
            for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = (row + row_step, col + col_step)
                if (neighbor in route_cells and
                        clearance[neighbor] >= threshold and
                        neighbor not in previous):
                    previous[neighbor] = (row, col)
                    queue.append(neighbor)
        if endpoints[1] in previous:
            cell = endpoints[1]
            while cell is not None:
                output[cell[0]][cell[1]] = 9
                cell = previous[cell]
            found = True
            break

    return output
