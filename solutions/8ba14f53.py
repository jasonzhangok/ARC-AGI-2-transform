from collections import deque


def _enclosed_zero_count(grid, color):
    height = len(grid)
    width = len(grid[0])
    reachable = set()
    queue = deque()

    for row in range(height):
        for col in (0, width - 1):
            if grid[row][col] != color and (row, col) not in reachable:
                reachable.add((row, col))
                queue.append((row, col))
    for col in range(width):
        for row in (0, height - 1):
            if grid[row][col] != color and (row, col) not in reachable:
                reachable.add((row, col))
                queue.append((row, col))

    while queue:
        row, col = queue.popleft()
        for next_row, next_col in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if (
                0 <= next_row < height
                and 0 <= next_col < width
                and grid[next_row][next_col] != color
                and (next_row, next_col) not in reachable
            ):
                reachable.add((next_row, next_col))
                queue.append((next_row, next_col))

    return sum(
        grid[row][col] == 0 and (row, col) not in reachable
        for row in range(height)
        for col in range(width)
    )


def transform(grid):
    colors = []
    for row in grid:
        for value in row:
            if value != 0 and value not in colors:
                colors.append(value)

    result = [[0, 0, 0] for _ in range(3)]
    output_row = 0
    for color in colors:
        enclosed_count = _enclosed_zero_count(grid, color)
        for index in range(enclosed_count):
            result[output_row + index // 3][index % 3] = color
        output_row += (enclosed_count + 2) // 3

    return result
