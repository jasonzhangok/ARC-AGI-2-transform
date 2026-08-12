def transform(grid):
    h, w = len(grid), len(grid[0])
    separator_row = next(r for r in range(h) if len(set(grid[r])) == 1)
    separator_color = grid[separator_row][0]
    separator_col = next(
        c for c in range(w)
        if all(grid[r][c] == separator_color for r in range(h)))

    def dominant(top, bottom, left, right):
        counts = {}
        for r in range(top, bottom):
            for c in range(left, right):
                value = grid[r][c]
                counts[value] = counts.get(value, 0) + 1
        return max(counts, key=counts.get)

    top_left = dominant(0, separator_row, 0, separator_col)
    top_right = dominant(0, separator_row, separator_col + 1, w)
    bottom_left = dominant(separator_row + 1, h, 0, separator_col)
    bottom_right = dominant(separator_row + 1, h, separator_col + 1, w)
    return [
        [top_left, separator_color, top_right],
        [separator_color, separator_color, separator_color],
        [bottom_left, separator_color, bottom_right],
    ]
