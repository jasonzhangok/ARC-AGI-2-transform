def transform(grid):
    """Recolor nonoverlapping green copies of the cyan template."""
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]
    template = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 8:
                template.append((row, col))
    if not template:
        output = result
    else:
        min_row = min((point[0] for point in template))
        min_col = min((point[1] for point in template))
        shape = [(row - min_row, col - min_col) for row, col in template]
        variants = []
        reflected = shape
        for reflection in range(2):
            rotated = reflected
            for turn in range(4):
                top = min((point[0] for point in rotated))
                left = min((point[1] for point in rotated))
                normalized = tuple(sorted(((row - top, col - left) for row, col in rotated)))
                if normalized not in variants:
                    variants.append(normalized)
                rotated = [(col, -row) for row, col in rotated]
            reflected = [(row, -col) for row, col in shape]
        candidates = []
        for variant in variants:
            shape_height = max((point[0] for point in variant)) + 1
            shape_width = max((point[1] for point in variant)) + 1
            for top in range(height - shape_height + 1):
                for left in range(width - shape_width + 1):
                    cells = tuple(((top + row, left + col) for row, col in variant))
                    if all((grid[row][col] == 3 for row, col in cells)):
                        candidates.append((top, left, cells))
        candidates.sort()
        claimed = set()
        for top, left, cells in candidates:
            if all((cell not in claimed for cell in cells)):
                for row, col in cells:
                    result[row][col] = 8
                    claimed.add((row, col))
        output = result
    return output
