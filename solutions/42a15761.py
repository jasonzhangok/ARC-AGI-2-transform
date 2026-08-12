def transform(grid):
    height, width = len(grid), len(grid[0])
    block_count = (width + 1) // 4
    blocks = [
        [row[4 * index:4 * index + 3] for row in grid]
        for index in range(block_count)
    ]
    blocks.sort(key=lambda block: sum(row[1] == 0 for row in block))
    output = []
    for row in range(height):
        combined = []
        for index, block in enumerate(blocks):
            if index:
                combined.append(0)
            combined.extend(block[row])
        output.append(combined)
    return output
