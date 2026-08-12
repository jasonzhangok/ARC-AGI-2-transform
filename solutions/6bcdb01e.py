def transform(grid):
    original = [row[:] for row in grid]
    result = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0])
    seeds = []
    for row in range(height):
        for col in range(width):
            if original[row][col] == 3:
                seeds.append((row, col))
    outer_row, outer_col = seeds[0]
    inner_row, inner_col = seeds[1]
    horizontal = seeds[0][0] == seeds[1][0]
    for row, col in seeds:
        if ((horizontal and (col == 0 or col == width - 1))
                or (not horizontal and (row == 0 or row == height - 1))):
            outer_row, outer_col = row, col
        else:
            inner_row, inner_col = row, col
    row = inner_row
    col = inner_col
    dr = inner_row - outer_row
    dc = inner_col - outer_col
    seen = set()
    while (row, col, dr, dc) not in seen:
        seen.add((row, col, dr, dc))
        next_row = row + dr
        next_col = col + dc
        if not (0 <= next_row < height and 0 <= next_col < width):
            break
        if original[next_row][next_col] == 8:
            choices = []
            for turn_row, turn_col in ((dc, -dr), (-dc, dr)):
                candidate_row = row + turn_row
                candidate_col = col + turn_col
                if (0 <= candidate_row < height and 0 <= candidate_col < width
                        and original[candidate_row][candidate_col] != 8):
                    choices.append((turn_row, turn_col))
            if len(choices) != 1:
                break
            dr, dc = choices[0]
        else:
            row = next_row
            col = next_col
            if result[row][col] == 7:
                result[row][col] = 3
    output = result
    return output
