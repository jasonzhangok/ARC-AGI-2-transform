from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    dominant = Counter(value for row in grid for value in row).most_common(1)[0][0]
    result = [[0] * (width * height) for _ in range(height * height)]
    for macro_r in range(height):
        for macro_c in range(width):
            if grid[macro_r][macro_c] == dominant:
                for r in range(height):
                    for c in range(width):
                        result[macro_r * height + r][macro_c * width + c] = grid[r][c]
    return result
