def transform(grid):
    rotated = [row[::-1] for row in grid[::-1]]
    strip = [row + row[::-1] + row for row in rotated]
    output = strip + strip[::-1] + strip
    return output
