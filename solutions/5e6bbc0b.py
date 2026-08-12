def transform(grid):
    """Pack the checkerboard's blue cells toward the edge marked by 8."""
    height = len(grid)
    if height == 0:
        output = []
    else:
        width = len(grid[0])
        marker_row, marker_col = next(
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == 8
        )
        if marker_col == 0 or marker_col == width - 1:
            toward_start = marker_col == 0
            output = []
            for row_index, row in enumerate(grid):
                blue_count = sum(cell == 1 for cell in row)
                if row_index == marker_row:
                    packed = [8] + [1] * blue_count + [9] * blue_count + [0] * (width - 1 - 2 * blue_count)
                else:
                    packed = [1] * blue_count + [0] * (width - blue_count)
                output.append(packed if toward_start else packed[::-1])
        else:
            toward_start = marker_row == 0
            output = [[0 for _ in range(width)] for _ in range(height)]
            for col in range(width):
                blue_count = sum(grid[row][col] == 1 for row in range(height))
                if col == marker_col:
                    packed = [8] + [1] * blue_count + [9] * blue_count + [0] * (height - 1 - 2 * blue_count)
                else:
                    packed = [1] * blue_count + [0] * (height - blue_count)
                if not toward_start:
                    packed = packed[::-1]
                for row, color in enumerate(packed):
                    output[row][col] = color
    return output
