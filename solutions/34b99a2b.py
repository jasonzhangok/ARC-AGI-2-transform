def transform(grid):
    return [
        [2 if (left != 0) != (right != 0) else 0 for left, right in zip(row[:4], row[5:])]
        for row in grid
    ]
