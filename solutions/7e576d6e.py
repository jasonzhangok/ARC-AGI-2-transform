def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1

    background = max(counts, key=counts.get)
    path_color = 0
    for color in counts:
        if counts[color] == 2:
            path_color = color

    full_rows = []
    for r in range(height):
        if all(grid[r][c] != background for c in range(width)):
            full_rows.append(r)
    full_columns = []
    for c in range(width):
        if all(grid[r][c] != background for r in range(height)):
            full_columns.append(c)

    result = [row[:] for row in grid]
    endpoints = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] == path_color:
                endpoints.append((r, c))

    if full_rows:
        endpoints.sort()
        current_r, current_c = endpoints[0]
        end_r, end_c = endpoints[1]
        for wall_r in full_rows:
            line_counts = {}
            for color in grid[wall_r]:
                line_counts[color] = line_counts.get(color, 0) + 1
            gate_color = min(line_counts, key=line_counts.get)
            gate_positions = []
            for c in range(width):
                if grid[wall_r][c] == gate_color:
                    gate_positions.append(c)
            gate_c = gate_positions[len(gate_positions) // 2]
            turn_r = wall_r - 1
            for r in range(min(current_r, turn_r), max(current_r, turn_r) + 1):
                result[r][current_c] = path_color
            for c in range(min(current_c, gate_c), max(current_c, gate_c) + 1):
                result[turn_r][c] = path_color
            result[wall_r][gate_c] = path_color
            current_r, current_c = wall_r, gate_c
        for r in range(min(current_r, end_r), max(current_r, end_r) + 1):
            result[r][current_c] = path_color
        for c in range(min(current_c, end_c), max(current_c, end_c) + 1):
            result[end_r][c] = path_color
    else:
        if endpoints[0][1] > endpoints[1][1]:
            endpoints[0], endpoints[1] = endpoints[1], endpoints[0]
        current_r, current_c = endpoints[0]
        end_r, end_c = endpoints[1]
        for wall_c in full_columns:
            line_counts = {}
            for r in range(height):
                color = grid[r][wall_c]
                line_counts[color] = line_counts.get(color, 0) + 1
            gate_color = min(line_counts, key=line_counts.get)
            gate_positions = []
            for r in range(height):
                if grid[r][wall_c] == gate_color:
                    gate_positions.append(r)
            gate_r = gate_positions[len(gate_positions) // 2]
            turn_c = wall_c - 1
            for c in range(min(current_c, turn_c), max(current_c, turn_c) + 1):
                result[current_r][c] = path_color
            for r in range(min(current_r, gate_r), max(current_r, gate_r) + 1):
                result[r][turn_c] = path_color
            result[gate_r][wall_c] = path_color
            current_r, current_c = gate_r, wall_c
        for c in range(min(current_c, end_c), max(current_c, end_c) + 1):
            result[current_r][c] = path_color
        for r in range(min(current_r, end_r), max(current_r, end_r) + 1):
            result[r][end_c] = path_color

    return result
