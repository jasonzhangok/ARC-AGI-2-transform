from collections import Counter
def transform(grid):
    bg=Counter(v for row in grid for v in row).most_common(1)[0][0];h,w=len(grid),len(grid[0])
    rows=sum(len(set(grid[r]))==1 and grid[r][0]!=bg for r in range(1,h-1));cols=sum(len(set(grid[r][c] for r in range(h)))==1 and grid[0][c]!=bg for c in range(1,w-1))
    return [[bg]*(cols+1) for _ in range(rows+1)]
