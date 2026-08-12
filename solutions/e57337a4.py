from collections import Counter


def transform(grid):
    color = Counter(value for row in grid for value in row if value != 0).most_common(1)[0][0]
    return [
        [0 if any(grid[r][c] == 0 for r in range(br * 5, br * 5 + 5) for c in range(bc * 5, bc * 5 + 5)) else color for bc in range(3)]
        for br in range(3)
    ]
