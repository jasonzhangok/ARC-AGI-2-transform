from collections import Counter


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    choices = []

    for size in range(3, min(height, width) + 1):
        squares = []
        for top in range(height - size + 1):
            for left in range(width - size + 1):
                square = tuple(
                    tuple(grid[row][left:left + size])
                    for row in range(top, top + size)
                )
                border = [
                    square[row][col]
                    for row in range(size)
                    for col in range(size)
                    if row in (0, size - 1) or col in (0, size - 1)
                ]
                interior = [
                    square[row][col]
                    for row in range(1, size - 1)
                    for col in range(1, size - 1)
                ]
                if (
                    all(value == 8 for value in border)
                    and all(value in (8, 2) for value in interior)
                    and 2 in interior
                ):
                    squares.append(square)

        frequencies = Counter(squares)
        if any(count >= 2 for count in frequencies.values()):
            unique = [square for square, count in frequencies.items() if count == 1]
            if len(unique) == 1:
                choices.append(unique[0])

    chosen = max(choices, key=len)
    return [list(row) for row in chosen]
