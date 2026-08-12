from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    candidates = []
    for r in range(height - 4):
        for c in range(width - 4):
            block = [row[c:c + 5] for row in grid[r:r + 5]]
            colors = [value for row in block for value in row if value != 0]
            if not colors:
                continue
            color = Counter(colors).most_common(1)[0][0]
            if not all(block[rr][cc] == color for rr, cc in ((0, 0), (0, 4), (4, 0), (4, 4))):
                continue
            top_clear = r == 0 or all(grid[r - 1][cc] == 0 for cc in range(c, c + 5))
            left_clear = c == 0 or all(grid[rr][c - 1] == 0 for rr in range(r, r + 5))
            if top_clear and left_clear:
                holes = sum(value == 0 for row in block for value in row)
                candidates.append((holes, block))
    frequencies = Counter(holes for holes, _ in candidates)
    return next(block for holes, block in candidates if frequencies[holes] == 1)
