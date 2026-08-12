def transform(grid):
    height = len(grid)
    width = len(grid[0])
    frame_color = grid[1][0]
    counts = {}

    for row in range(2, height - 1):
        for col in range(1, width - 1):
            color = grid[row][col]
            if color != 0 and color != frame_color:
                counts[color] = counts.get(color, 0) + 1

    target = max(counts, key=counts.get)
    positions = []
    for row in range(2, height - 1):
        for col in range(1, width - 1):
            if grid[row][col] == target:
                positions.append((row, col))

    top = min(row for row, col in positions)
    bottom = max(row for row, col in positions)
    left = min(col for row, col in positions)
    right = max(col for row, col in positions)

    output = [grid[0][:]] + [[0] * width for row in range(1, height)]
    for row in range(1, height):
        for col in range(width):
            if row == 1 or row == height - 1 or col == 0 or col == width - 1:
                output[row][col] = target
            elif (row == top or row == bottom) and left <= col <= right:
                output[row][col] = target
            elif (col == left or col == right) and top <= row <= bottom:
                output[row][col] = target

    return output
