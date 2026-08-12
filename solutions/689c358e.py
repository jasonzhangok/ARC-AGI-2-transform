def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]
    if height < 3 or width < 3:
        return result

    border_color = grid[0][0]
    counts = {}
    for row in range(1, height - 1):
        for column in range(1, width - 1):
            color = grid[row][column]
            counts[color] = counts.get(color, 0) + 1
    background_color = max(counts, key=counts.get)

    for row in range(1, height - 1):
        for column in range(1, width - 1):
            color = grid[row][column]
            if color == border_color or color == background_color:
                continue
            if not (grid[row - 1][column] == color and
                    grid[row + 1][column] == color and
                    grid[row][column - 1] == color and
                    grid[row][column + 1] == color):
                continue

            up = 0
            position = row - 1
            while position >= 0 and grid[position][column] == color:
                up += 1
                position -= 1
            down = 0
            position = row + 1
            while position < height and grid[position][column] == color:
                down += 1
                position += 1
            left = 0
            position = column - 1
            while position >= 0 and grid[row][position] == color:
                left += 1
                position -= 1
            right = 0
            position = column + 1
            while position < width and grid[row][position] == color:
                right += 1
                position += 1

            if up != down and left == right:
                if up < down:
                    result[0][column] = color
                    result[height - 1][column] = 0
                else:
                    result[height - 1][column] = color
                    result[0][column] = 0
            elif left != right and up == down:
                if left < right:
                    result[row][0] = color
                    result[row][width - 1] = 0
                else:
                    result[row][width - 1] = color
                    result[row][0] = 0

    return result
