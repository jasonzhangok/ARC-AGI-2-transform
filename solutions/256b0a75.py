def transform(grid):
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]
    top = -1
    bottom = -1
    left = -1
    right = -1
    fill = 0
    best_area = -1

    for t in range(height - 3):
        for b in range(t + 3, height):
            for l in range(width - 3):
                for r in range(l + 3, width):
                    tl = grid[t][l]
                    tr = grid[t][r]
                    bl = grid[b][l]
                    br = grid[b][r]
                    if (tl != 0 and tr != 0 and bl != 0 and br != 0
                            and grid[t][l + 1] == tl
                            and grid[t + 1][l] == tl
                            and grid[t][r - 1] == tr
                            and grid[t + 1][r] == tr
                            and grid[b][l + 1] == bl
                            and grid[b - 1][l] == bl
                            and grid[b][r - 1] == br
                            and grid[b - 1][r] == br):
                        corners = [tl, tr, bl, br]
                        if corners.count(8) == 3:
                            area = (b - t + 1) * (r - l + 1)
                            if area > best_area:
                                top = t
                                bottom = b
                                left = l
                                right = r
                                best_area = area
                                for color in corners:
                                    if color != 8:
                                        fill = color

    if top == -1:
        return result

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0 and (top <= i <= bottom or left <= j <= right):
                result[i][j] = fill

    for i in range(height):
        for j in range(width):
            color = grid[i][j]
            if color != 0 and left <= j <= right:
                if i < top:
                    for k in range(i + 1):
                        if grid[k][j] == 0:
                            result[k][j] = color
                elif i > bottom:
                    for k in range(i, height):
                        if grid[k][j] == 0:
                            result[k][j] = color
            if color != 0 and top <= i <= bottom:
                if j < left:
                    for k in range(j + 1):
                        if grid[i][k] == 0:
                            result[i][k] = color
                elif j > right:
                    for k in range(j, width):
                        if grid[i][k] == 0:
                            result[i][k] = color

    for j in range(left, right + 1):
        result[top][j] = 8
        result[bottom][j] = 8
    for i in range(top, bottom + 1):
        result[i][left] = 8
        result[i][right] = 8

    return result
