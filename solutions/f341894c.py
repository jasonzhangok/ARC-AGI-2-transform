"""Orient two-cell coloured markers toward border guides."""


def transform(grid):
    """Put colour 6 on the end of each 1/6 domino nearest its border 7."""
    height = len(grid)
    width = len(grid[0]) if height else 0
    output = [row[:] for row in grid]

    for row in range(height):
        for column in range(width):
            if grid[row][column] != 7:
                continue

            directions = []
            if row == 0:
                directions.append((1, 0))
            if row == height - 1:
                directions.append((-1, 0))
            if column == 0:
                directions.append((0, 1))
            if column == width - 1:
                directions.append((0, -1))

            for delta_row, delta_column in directions:
                near_row = row + delta_row
                near_column = column + delta_column
                while (
                    0 <= near_row < height
                    and 0 <= near_column < width
                    and grid[near_row][near_column] not in (1, 6)
                ):
                    near_row += delta_row
                    near_column += delta_column

                far_row = near_row + delta_row
                far_column = near_column + delta_column
                if not (
                    0 <= near_row < height
                    and 0 <= near_column < width
                    and 0 <= far_row < height
                    and 0 <= far_column < width
                ):
                    continue
                if {grid[near_row][near_column], grid[far_row][far_column]} != {1, 6}:
                    continue

                output[near_row][near_column] = 6
                output[far_row][far_column] = 1

    return output
