def transform(grid):
    original_size = len(grid)
    output = [row[:] for row in grid]
    center_color = grid[original_size // 2][original_size // 2]
    middle_color = grid[original_size // 2 - 1][original_size // 2 - 1]
    corner_color = grid[0][0]
    cycle = [center_color, middle_color, corner_color]
    current_color = grid[-1][-1]

    while len(output) < 2 * original_size:
        current_index = cycle.index(current_color)
        next_color = cycle[(current_index + 1) % len(cycle)]
        size = len(output)
        for row in output:
            row.append(current_color)
        output.append([current_color for _ in range(size)] + [next_color])
        current_color = next_color
    return output
