def transform(grid):
    rotated = [
        [grid[row][col] for row in range(len(grid))]
        for col in range(len(grid[0]) - 1, -1, -1)
    ]
    inner_height = len(rotated)
    inner_width = len(rotated[0])
    output = []
    border = [7] + [1] * inner_width + [7]
    for copy_index in range(2):
        output.append(border[:])
        for row in rotated:
            output.append([1] + row[:] + [1])
    output.append(border[:])
    return output
