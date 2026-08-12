from collections import Counter


def transform(grid):
    bg=Counter(v for row in grid for v in row).most_common(1)[0][0]
    top=grid[0][:]
    middle=grid[1][:]
    bottom=[6 if v!=bg else bg for v in top]
    return [top,middle,bottom]
