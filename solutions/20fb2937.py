from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    separator_row = next(
        row
        for row in range(height)
        if len(set(grid[row])) == 1 and grid[row][0] not in (background, 0)
    )
    header_end = next(row for row in range(separator_row) if all(value == background for value in grid[row]))
    mapping = {}
    for row in range(header_end + 1, separator_row):
        for col, marker in enumerate(grid[row]):
            if marker != background:
                header_color = next(
                    grid[r][col]
                    for r in range(header_end)
                    if grid[r][col] != background
                )
                mapping[marker] = header_color
    lower = grid[separator_row + 1:]
    output = [[background] * width for _ in lower]
    for row, values in enumerate(lower):
        for col, marker in enumerate(values):
            if marker not in mapping:
                continue
            color = mapping[marker]
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    y, x = row + dr, col + dc
                    if 0 <= y < len(output) and 0 <= x < width:
                        output[y][x] = color
    return output
