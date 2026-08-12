from collections import Counter


def transform(grid):
    frequencies = Counter(value for row in grid for value in row)
    marker = min(frequencies, key=frequencies.get)
    region_counts = Counter()
    h, w = len(grid), len(grid[0])
    for r in range(h):
        for c in range(w):
            if grid[r][c] != marker:
                continue
            neighbors = Counter(
                grid[x][y]
                for x in range(max(0, r - 1), min(h, r + 2))
                for y in range(max(0, c - 1), min(w, c + 2))
                if grid[x][y] != marker
            )
            if neighbors:
                region_counts[neighbors.most_common(1)[0][0]] += 1
    return [[region_counts.most_common(1)[0][0]]]
