def transform(grid):
    height = len(grid)
    separator_columns = [
        col
        for col in range(len(grid[0]))
        if all(grid[row][col] == 0 for row in range(height))
    ]

    blocks = []
    start = 0
    for separator in separator_columns + [len(grid[0])]:
        if start < separator:
            blocks.append([row[start:separator] for row in grid])
        start = separator + 1

    colors = []
    for block in blocks:
        block_height = len(block)
        block_width = len(block[0])
        empty = {
            (row, col)
            for row in range(block_height)
            for col in range(block_width)
            if block[row][col] == 0
        }
        if not empty:
            color = 2
        elif any(row == block_height - 1 for row, _ in empty):
            color = 4
        elif any(col in (0, block_width - 1) for _, col in empty):
            color = 3
        else:
            color = 8
        colors.append(color)

    output = [[color] * len(colors) for color in colors]
    return output
