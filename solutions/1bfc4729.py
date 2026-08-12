def transform(grid):
    height, width = len(grid), len(grid[0])
    markers = [(r, c, grid[r][c]) for r in range(height) for c in range(width) if grid[r][c] != 0]
    markers.sort()
    split = (markers[0][0] + markers[1][0]) // 2
    output = [[0] * width for _ in range(height)]
    for index, (top, bottom, marker) in enumerate(((0, split, markers[0]), (split + 1, height - 1, markers[1]))):
        color = marker[2]
        for row in range(top, bottom + 1):
            output[row][0] = color
            output[row][-1] = color
            outward = row <= marker[0] if index == 0 else row >= marker[0]
            if outward and (row - marker[0]) % 2 == 0:
                output[row] = [color] * width
    return output
