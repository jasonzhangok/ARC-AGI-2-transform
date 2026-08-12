def transform(grid):
    try:
        output = [row[:] for row in grid]
        cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
        r0, r1 = (min((r for r, _ in cells)), max((r for r, _ in cells)))
        c0, c1 = (min((c for _, c in cells)), max((c for _, c in cells)))
        for r in range(r0 + 1, r1):
            if all((grid[r][c] == 0 for c in range(c0, c1 + 1))):
                output[r] = [3] * len(grid[0])
                raise StopIteration(output)
        for c in range(c0 + 1, c1):
            if all((grid[r][c] == 0 for r in range(r0, r1 + 1))):
                for r in range(len(grid)):
                    output[r][c] = 3
                raise StopIteration(output)
        raise StopIteration(output)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
