def transform(grid):
    out = [row[:] for row in grid]
    n = len(out)

    def solve(pos):
        if pos == n * n:
            return True
        r, c = divmod(pos, n)
        if out[r][c] != 0:
            return solve(pos + 1)
        used = set(out[r]) | {out[y][c] for y in range(n)}
        for value in range(1, n + 1):
            if value not in used:
                out[r][c] = value
                if solve(pos + 1):
                    return True
        out[r][c] = 0
        return False

    solve(0)
    return out
