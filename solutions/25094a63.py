def transform(grid):
    height = len(grid)
    width = len(grid[0])
    marked = set()

    for top in range(height - 3):
        for left in range(width - 3):
            color = grid[top][left]
            solid = True
            for row_offset in range(4):
                for col_offset in range(4):
                    if grid[top + row_offset][left + col_offset] != color:
                        solid = False
            if solid:
                for row_offset in range(4):
                    for col_offset in range(4):
                        marked.add((top + row_offset, left + col_offset))

    output = [row[:] for row in grid]
    for row, col in marked:
        output[row][col] = 4

    return output
