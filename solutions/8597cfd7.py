def transform(grid):
    divider=next(r for r,row in enumerate(grid) if row.count(5)==len(row))
    colors=sorted(set(v for row in grid for v in row)-{0,5})
    score={color:abs(sum(grid[r][c]==color for r in range(divider) for c in range(len(grid[0])))-sum(grid[r][c]==color for r in range(divider+1,len(grid)) for c in range(len(grid[0])))) for color in colors}
    color=max(colors,key=lambda c:(score[c],-c))
    return [[color,color],[color,color]]
