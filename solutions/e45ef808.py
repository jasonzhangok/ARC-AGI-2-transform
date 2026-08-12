def transform(grid):
    height, width = len(grid), len(grid[0])
    one_heights = []
    for col in range(width):
        amount = 0
        for row in range(1, height):
            if grid[row][col] != 1:
                break
            amount += 1
        one_heights.append(amount)

    tallest_col = max(range(width), key=lambda col: one_heights[col])
    shortest_height = min(height for height in one_heights if height > 0)
    shortest_col = max(
        col for col in range(width) if one_heights[col] == shortest_height
    )
    output = [row[:] for row in grid]
    for row in range(1, height):
        if output[row][tallest_col] == 1:
            output[row][tallest_col] = 9
        if output[row][shortest_col] == 1:
            output[row][shortest_col] = 4
    return output
