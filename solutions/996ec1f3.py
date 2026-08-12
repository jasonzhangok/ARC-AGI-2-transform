def transform(grid):
    h, w = len(grid), len(grid[0])
    separator_row = next(r for r in range(h) if len(set(grid[r])) == 1)
    separator_color = grid[separator_row][0]
    separator_col = next(
        c for c in range(w)
        if all(grid[r][c] == separator_color for r in range(h)))

    dominant_colors = []
    for top, bottom, left, right in (
        (0, separator_row, 0, separator_col),
        (0, separator_row, separator_col + 1, w),
        (separator_row + 1, h, 0, separator_col),
        (separator_row + 1, h, separator_col + 1, w),
    ):
        counts = {}
        for r in range(top, bottom):
            for c in range(left, right):
                value = grid[r][c]
                counts[value] = counts.get(value, 0) + 1
        best_color = None
        for value, count in counts.items():
            if best_color is None or count > counts[best_color]:
                best_color = value
        dominant_colors.append(best_color)
    top_left, top_right, bottom_left, bottom_right = dominant_colors
    output = [
        [top_left, separator_color, top_right],
        [separator_color, separator_color, separator_color],
        [bottom_left, separator_color, bottom_right],
    ]
    return output
