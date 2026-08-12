

def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for cell_value in (value for row in grid for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    background = max(counts, key=counts.get)
    marker = min((value for value in counts if value != background), key=counts.get)
    points = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == marker}
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    corners = {(top, left), (top, right), (bottom, left), (bottom, right)}
    missing = next(corner for corner in corners if corner not in points)
    output = [row[:] for row in grid]

    mr, mc = missing
    for col in range(left, right + 1):
        output[mr][col] = marker if grid[mr][col] == marker else 8
    for row in range(top, bottom + 1):
        output[row][mc] = marker if grid[row][mc] == marker else 8

    size = bottom - top
    for offset in range(size + 1):
        row = top + offset
        if missing in ((top, left), (bottom, right)):
            col = right - offset
        else:
            col = left + offset
        output[row][col] = marker if grid[row][col] == marker else 8
    return output
