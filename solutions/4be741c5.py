from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    lines = grid if h > w else [[grid[r][c] for r in range(h)] for c in range(w)]
    dominant = [Counter(line).most_common(1)[0][0] for line in lines]
    sequence = []
    for color in dominant:
        if not sequence or sequence[-1] != color:
            sequence.append(color)
    return [[v] for v in sequence] if h > w else [sequence]
