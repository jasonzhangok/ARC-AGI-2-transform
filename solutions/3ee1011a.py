from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row if value != 0)
    layers = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    size = layers[0][1]
    result = [[0 for _ in range(size)] for _ in range(size)]
    for inset, (color, _) in enumerate(layers):
        low, high = inset, size - 1 - inset
        for position in range(low, high + 1):
            result[low][position] = color
            result[high][position] = color
            result[position][low] = color
            result[position][high] = color
    return result
