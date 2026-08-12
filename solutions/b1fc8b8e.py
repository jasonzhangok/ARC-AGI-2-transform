from itertools import combinations


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colored = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    }

    template = None
    for mask in range(1, 16):
        shape = {
            (row, col)
            for row in range(2)
            for col in range(2)
            if mask & (1 << (2 * row + col))
        }
        copies = []
        for top in range(height - 1):
            for left in range(width - 1):
                cells = {(top + row, left + col) for row, col in shape}
                if cells <= colored:
                    copies.append(cells)

        for choice in combinations(copies, 4):
            union = set().union(*choice)
            if sum(map(len, choice)) == len(union) and union == colored:
                template = shape
                break
        if template is not None:
            break

    output = [[0] * 5 for _ in range(5)]
    for top, left in ((0, 0), (0, 3), (3, 0), (3, 3)):
        for row, col in template:
            output[top + row][left + col] = 8
    return output
