def transform(grid):
    h, w = len(grid), len(grid[0])
    background = grid[-1][-1]
    rows = [r for r in range(h) if any(v != background for v in grid[r])]
    cols = [c for c in range(w) if any(grid[r][c] != background for r in range(h))]
    sample = [grid[r][:max(cols) + 1] for r in range(max(rows) + 1)]
    sh, sw = len(sample), len(sample[0])
    pr = next(p for p in range(1, sh + 1)
              if all(sample[r][c] == sample[r % p][c] for r in range(sh) for c in range(sw)))
    pc = next(p for p in range(1, sw + 1)
              if all(sample[r][c] == sample[r][c % p] for r in range(sh) for c in range(sw)))
    output = [[sample[r % pr][(c + 1) % pc] for c in range(w)] for r in range(h)]
    return output
