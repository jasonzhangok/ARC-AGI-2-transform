def transform(grid):
    height = len(grid)
    width = len(grid[0])

    counts = {}
    for row in grid:
        for value in row:
            if value not in (0, 1):
                counts[value] = counts.get(value, 0) + 1
    marker_color = max(counts, key=counts.get)

    seen = set()
    corners = []
    for start_row in range(height):
        for start_column in range(width):
            if (
                grid[start_row][start_column] != marker_color
                or (start_row, start_column) in seen
            ):
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
                        and grid[next_row][next_column] == marker_color
                        and (next_row, next_column) not in seen
                    ):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))

            top = min(row for row, column in component)
            left = min(column for row, column in component)
            occupied = {(row - top, column - left) for row, column in component}
            missing = next(
                (row, column)
                for row in range(2)
                for column in range(2)
                if (row, column) not in occupied
            )
            if missing == (1, 1):
                role = "top_left"
            elif missing == (1, 0):
                role = "top_right"
            elif missing == (0, 1):
                role = "bottom_left"
            else:
                role = "bottom_right"
            corners.append((top, left, role))

    corner_roles = {(row, column): role for row, column, role in corners}
    rectangles = []
    for top, left, role in corners:
        if role != "top_left":
            continue
        for same_top, right, right_role in corners:
            if same_top != top or right <= left or right_role != "top_right":
                continue
            for bottom, same_left, bottom_role in corners:
                if (
                    bottom > top
                    and same_left == left
                    and bottom_role == "bottom_left"
                    and corner_roles.get((bottom, right)) == "bottom_right"
                ):
                    rectangles.append((top, bottom + 1, left, right + 1))

    output = [[0 if value == 1 else value for value in row] for row in grid]
    for top, bottom, left, right in rectangles:
        for row in range(top, bottom + 1):
            for column in range(left, right + 1):
                if grid[row][column] != 1:
                    continue
                output[row][column] = 1
                if bottom - top > right - left:
                    reflected_row = top + bottom - row
                    reflected_column = column
                else:
                    reflected_row = row
                    reflected_column = left + right - column
                if output[reflected_row][reflected_column] == 0:
                    output[reflected_row][reflected_column] = 1

    return output
