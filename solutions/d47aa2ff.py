def transform(grid):
    height = len(grid)
    panel_width = (len(grid[0]) - 1) // 2
    output = []

    for row in range(height):
        left = grid[row][:panel_width]
        right = grid[row][panel_width + 1:]
        result_row = []
        for left_value, right_value in zip(left, right):
            if left_value == right_value:
                result_row.append(left_value)
            elif left_value == 0:
                result_row.append(1)
            else:
                result_row.append(2)
        output.append(result_row)
    return output
