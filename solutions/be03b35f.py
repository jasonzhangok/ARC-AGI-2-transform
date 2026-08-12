def transform(grid):
    panels = [
        tuple(tuple(grid[row + drow][col + dcol] for dcol in range(2)) for drow in range(2))
        for row, col in ((0, 0), (0, 3), (3, 0), (3, 3))
    ]
    patterns = [panel for panel in panels if 1 in panel[0] or 1 in panel[1]]

    def rotate(pattern):
        return tuple(tuple(pattern[1 - col][row] for col in range(2)) for row in range(2))

    candidates = []
    pattern = patterns[0]
    for _ in range(4):
        if pattern not in candidates:
            candidates.append(pattern)
        pattern = rotate(pattern)
    present = set(patterns)
    missing = next(candidate for candidate in candidates if candidate not in present)
    return [list(row) for row in missing]
