def transform(grid):
    output = [row[:] for row in grid]
    colors = sorted({value for row in grid for value in row if value != 0})

    boxes = {}
    for color in colors:
        cells = [
            (row, col)
            for row, line in enumerate(grid)
            for col, value in enumerate(line)
            if value == color
        ]
        boxes[color] = (
            min(row for row, _ in cells),
            max(row for row, _ in cells),
            min(col for _, col in cells),
            max(col for _, col in cells),
        )

    first, second = colors
    first_box = boxes[first]
    second_box = boxes[second]
    top = max(first_box[0], second_box[0])
    bottom = min(first_box[1], second_box[1])
    left = max(first_box[2], second_box[2])
    right = min(first_box[3], second_box[3])

    visible_color = grid[top][left]
    hidden_color = second if visible_color == first else first
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            output[row][col] = hidden_color
    return output
