def transform(grid):
    height, width = len(grid), len(grid[0])
    largest = (0, 0, 0)
    for size in range(1, min(height, width) + 1):
        for top in range(height - size + 1):
            for left in range(width - size + 1):
                if all(
                    grid[row][col] != 0
                    for row in range(top, top + size)
                    for col in range(left, left + size)
                ):
                    largest = max(largest, (size, top, left))

    size, top, left = largest
    center_row_twice = 2 * top + size - 1
    center_col_twice = 2 * left + size - 1
    output = [row[:] for row in grid]

    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color == 0:
                continue
            rotated_row = 2 * row
            rotated_col = 2 * col
            for _ in range(4):
                if rotated_row % 2 == 0 and rotated_col % 2 == 0:
                    new_row = rotated_row // 2
                    new_col = rotated_col // 2
                    if 0 <= new_row < height and 0 <= new_col < width:
                        output[new_row][new_col] = color
                rotated_row, rotated_col = (
                    center_row_twice - (rotated_col - center_col_twice),
                    center_col_twice + (rotated_row - center_row_twice),
                )
    return output
