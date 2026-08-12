from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    candidates = []
    for period in range(1, h // 2 + 1):
        mismatches = 0
        for phase in range(period):
            for c in range(w):
                values = [grid[r][c] for r in range(phase, h, period)]
                mismatches += len(values) - Counter(values).most_common(1)[0][1]
        candidates.append((mismatches, period))
    _, period = min(candidates)
    pattern = []
    for phase in range(period):
        row = []
        for c in range(w):
            values = [grid[r][c] for r in range(phase, h, period)]
            row.append(Counter(values).most_common(1)[0][0])
        pattern.append(row)
    return [pattern[r % period][:] for r in range(h)]
