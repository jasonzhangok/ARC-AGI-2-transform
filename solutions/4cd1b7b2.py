def transform(grid):
    out = [row[:] for row in grid]
    n = len(out)

    empty = [(row, col) for row in range(n) for col in range(n) if out[row][col] == 0]
    choices = [0] * len(empty)
    index = 0
    while 0 <= index < len(empty):
        row, col = empty[index]
        used = set(out[row]) | {out[y][col] for y in range(n)}
        value = choices[index] + 1
        while value <= n and value in used:
            value += 1
        if value <= n:
            out[row][col] = value
            choices[index] = value
            index += 1
        else:
            out[row][col] = 0
            choices[index] = 0
            index -= 1
            if index >= 0:
                previous_row, previous_col = empty[index]
                out[previous_row][previous_col] = 0
    output = out
    return output
