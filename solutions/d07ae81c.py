def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1

    backgrounds = sorted(counts, key=counts.get, reverse=True)[:2]
    seeds = []
    replacements = {}
    for row in range(height):
        for col in range(width):
            marker = grid[row][col]
            if marker in backgrounds:
                continue
            seeds.append((row, col))
            neighbor_counts = {backgrounds[0]: 0, backgrounds[1]: 0}
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = row + dr, col + dc
                    if (dr != 0 or dc != 0) and 0 <= nr < height and 0 <= nc < width:
                        neighbor = grid[nr][nc]
                        if neighbor in neighbor_counts:
                            neighbor_counts[neighbor] += 1
            underlying = backgrounds[0]
            if neighbor_counts[backgrounds[1]] > neighbor_counts[backgrounds[0]]:
                underlying = backgrounds[1]
            replacements[underlying] = marker

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] not in replacements:
                continue
            for seed_row, seed_col in seeds:
                if abs(row - seed_row) == abs(col - seed_col):
                    output[row][col] = replacements[grid[row][col]]
                    break
    return output
