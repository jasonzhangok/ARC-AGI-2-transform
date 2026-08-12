def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seed_row = next(row for row in range(height) if 7 in grid[row])
    state = [grid[seed_row][col] == 7 for col in range(width)]
    output = [row[:] for row in grid]

    generation = 1
    row = seed_row + 2
    while row < height:
        next_state = []
        for col in range(width):
            left = state[col - 1] if col > 0 else False
            center = state[col]
            right = state[col + 1] if col + 1 < width else False
            next_state.append(left and not center and right)

        color = 6 if generation % 2 == 1 else 7
        for col, active in enumerate(next_state):
            if active:
                output[row][col] = color
        state = next_state
        generation += 1
        row += 2

    return output
