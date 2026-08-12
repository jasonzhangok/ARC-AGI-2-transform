def transform(grid):
    try:
        sevens = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 7]
        r0, r1 = (min((r for r, _ in sevens)), max((r for r, _ in sevens)))
        c0, c1 = (min((c for _, c in sevens)), max((c for _, c in sevens)))
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                color = grid[r][c]
                border = [grid[r][c], grid[r][c + 1], grid[r][c + 2], grid[r + 1][c], grid[r + 1][c + 2], grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]]
                if color not in (0, 5, 7) and all((value == color for value in border)) and (r0 <= r + 1 <= r1) and (c0 <= c + 1 <= c1):
                    raise StopIteration([row[c:c + 3] for row in grid[r:r + 3]])
        raise StopIteration([[]])
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
