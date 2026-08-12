from collections import Counter


def transform(grid):
    background = Counter(
        value for row in grid for value in row
    ).most_common(1)[0][0]
    colors = {value for row in grid for value in row if value != background}
    objects = []
    output_size = 0

    for color in colors:
        cells = [
            (row, col)
            for row, line in enumerate(grid)
            for col, value in enumerate(line)
            if value == color
        ]
        top = min(row for row, _ in cells)
        bottom = max(row for row, _ in cells)
        left = min(col for _, col in cells)
        right = max(col for _, col in cells)
        output_size = max(
            output_size, bottom - top + 1, right - left + 1
        )
        objects.append((color, cells, (top + bottom) // 2, (left + right) // 2))

    center = output_size // 2
    output = [[background] * output_size for _ in range(output_size)]
    for color, cells, center_row, center_col in objects:
        for row, col in cells:
            output[center + row - center_row][center + col - center_col] = color
    return output
