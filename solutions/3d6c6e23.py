def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [[0 for col in range(width)] for row in range(height)]

    for center_col in range(width):
        counts = {}
        total = 0
        for row in range(height):
            color = grid[row][center_col]
            if color != 0:
                counts[color] = counts.get(color, 0) + 1
                total += 1
        if total == 0:
            continue
        levels = 1
        while (levels + 1) * (levels + 1) <= total:
            levels += 1
        remaining = dict(counts)
        for level in range(levels):
            span = 2 * level + 1
            chosen_color = 0
            for color in remaining:
                if remaining[color] >= span:
                    chosen_color = color
                    break
            row = height - levels + level
            for col in range(center_col - level, center_col + level + 1):
                if 0 <= col < width:
                    output[row][col] = chosen_color
            remaining[chosen_color] -= span

    return output
