def transform(grid):
    output = [row[:] for row in grid]
    markers = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] not in (0, 1):
                markers.append((
                    row // 3, col // 3,
                    row % 3, col % 3,
                    grid[row][col],
                ))

    for first in markers:
        for second in markers:
            if (first[4] != second[4]
                    or (first[2], first[3]) != (second[2], second[3])):
                continue
            if first[0] == second[0]:
                for block_col in range(
                        min(first[1], second[1]), max(first[1], second[1]) + 1):
                    output[first[0] * 3 + first[2]][block_col * 3 + first[3]] = first[4]
            if first[1] == second[1]:
                for block_row in range(
                        min(first[0], second[0]), max(first[0], second[0]) + 1):
                    output[block_row * 3 + first[2]][first[1] * 3 + first[3]] = first[4]
    return output
