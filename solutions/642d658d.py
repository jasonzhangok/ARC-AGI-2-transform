from collections import Counter

def transform(grid):
    h, w = len(grid), len(grid[0])
    crosses = Counter()
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] != 4:
                continue
            arms = [grid[r-1][c], grid[r+1][c], grid[r][c-1], grid[r][c+1]]
            if arms[0] != 0 and len(set(arms)) == 1:
                crosses[arms[0]] += 1
    return [[max(crosses, key=crosses.get)]]
