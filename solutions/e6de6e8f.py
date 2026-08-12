def transform(grid):
    instructions = []
    column = 0
    while column < len(grid[0]):
        if grid[0][column] == 0 and grid[1][column] == 0:
            column += 1
            continue

        start = column
        while (
            column < len(grid[0])
            and (grid[0][column] != 0 or grid[1][column] != 0)
        ):
            column += 1

        if column - start == 1:
            instructions.append(0)
        elif grid[0][start] == 0:
            instructions.append(-1)
        else:
            instructions.append(1)

    turns = sum(direction != 0 for direction in instructions)
    height = 1 + sum(2 if direction == 0 else 1 for direction in instructions)
    output = [[0 for _ in range(2 * turns + 1)] for _ in range(height)]

    row = 0
    position = turns
    output[row][position] = 3
    for direction in instructions:
        if direction == 0:
            for _ in range(2):
                row += 1
                output[row][position] = 2
        else:
            row += 1
            next_position = position + direction
            output[row][min(position, next_position)] = 2
            output[row][max(position, next_position)] = 2
            position = next_position

    return output
