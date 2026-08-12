

def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for cell_value in (value for row in grid for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    special = next(
        value
        for value in counts
        if value not in (0, 1, 4)
    )
    used = set()
    blocks = []
    for row in range(height - 1):
        for col in range(width - 1):
            cells = {(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)}
            if not cells & used and all(grid[r][c] == special for r, c in cells):
                blocks.append((row, col))
                used |= cells

    origin_row = min(row for row, _ in blocks)
    origin_col = min(col for _, col in blocks)
    pattern = {
        ((row - origin_row) // 2, (col - origin_col) // 2)
        for row, col in blocks
    }
    output = [row[:] for row in grid]
    for tile_row in range(0, height, 4):
        for tile_col in range(0, width, 4):
            if tile_row + 2 >= height or tile_col + 2 >= width:
                continue
            if any(grid[tile_row + r][tile_col + c] == special for r in range(3) for c in range(3)):
                continue
            if all(grid[tile_row + r][tile_col + c] == 1 for r, c in pattern):
                for r, c in pattern:
                    output[tile_row + r][tile_col + c] = special
    return output
