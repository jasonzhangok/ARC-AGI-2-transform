def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    remaining = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 8:
                remaining.add((row, col))

    while remaining:
        start = remaining.pop()
        component = {start}
        stack = [start]
        while stack:
            row, col = stack.pop()
            for neighbor in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        top = min(row for row, col in component)
        bottom = max(row for row, col in component)
        left = min(col for row, col in component)
        right = max(col for row, col in component)
        doubled_middle_row = top + bottom
        doubled_middle_col = left + right
        for row, col in component:
            if top + 2 <= row <= bottom - 2 and left + 2 <= col <= right - 2:
                output[row][col] = 4
            elif 2 * row <= doubled_middle_row:
                if 2 * col <= doubled_middle_col:
                    output[row][col] = 6
                else:
                    output[row][col] = 1
            else:
                if 2 * col <= doubled_middle_col:
                    output[row][col] = 2
                else:
                    output[row][col] = 3

    return output
