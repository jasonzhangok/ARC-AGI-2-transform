def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [[0 for _ in range(width)] for _ in range(height)]
    seen = set()

    for start_row in range(height):
        for start_column in range(width):
            if grid[start_row][start_column] != 3 or (start_row, start_column) in seen:
                continue
            stack = [(start_row, start_column)]
            seen.add((start_row, start_column))
            component = []
            while stack:
                row, column = stack.pop()
                component.append((row, column))
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_column < width
                        and grid[next_row][next_column] == 3
                        and (next_row, next_column) not in seen
                    ):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))

            cells = set(component)
            has_branch = False
            corners = 0
            for row, column in component:
                neighbors = [
                    (next_row, next_column)
                    for next_row, next_column in (
                        (row - 1, column),
                        (row + 1, column),
                        (row, column - 1),
                        (row, column + 1),
                    )
                    if (next_row, next_column) in cells
                ]
                if len(neighbors) >= 3:
                    has_branch = True
                if (
                    len(neighbors) == 2
                    and neighbors[0][0] != neighbors[1][0]
                    and neighbors[0][1] != neighbors[1][1]
                ):
                    corners += 1

            color = 2 if has_branch else (1 if corners == 1 else 6)
            for row, column in component:
                output[row][column] = color

    return output
