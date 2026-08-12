def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    colors = []
    for value in counts:
        if value != background and value != 8:
            colors.append(value)

    for color in colors:
        terminals = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    terminals.add((row, col))
        if len(terminals) < 2:
            continue

        ordered_terminals = sorted(terminals)
        for first_index in range(len(ordered_terminals)):
            first = ordered_terminals[first_index]
            for second_index in range(first_index + 1, len(ordered_terminals)):
                second = ordered_terminals[second_index]
                path = []
                if first[0] == second[0]:
                    for col in range(min(first[1], second[1]),
                                     max(first[1], second[1]) + 1):
                        path.append((first[0], col))
                elif first[1] == second[1]:
                    for row in range(min(first[0], second[0]),
                                     max(first[0], second[0]) + 1):
                        path.append((row, first[1]))
                if path and all(output[row][col] in (background, color)
                                for row, col in path):
                    for row, col in path:
                        output[row][col] = color

        network = set()
        for row in range(height):
            for col in range(width):
                if output[row][col] == color:
                    network.add((row, col))
        connected = {min(network)}
        stack = list(connected)
        while stack:
            row, col = stack.pop()
            for row_step, col_step in directions:
                neighbor = (row + row_step, col + col_step)
                if neighbor in network and neighbor not in connected:
                    connected.add(neighbor)
                    stack.append(neighbor)

        while not network <= connected:
            costs = {}
            previous = {}
            unvisited = []
            for row, col in connected:
                orientations = []
                for direction, step in enumerate(directions):
                    if (row - step[0], col - step[1]) in connected:
                        orientations.append(direction)
                if not orientations:
                    orientations.append(-1)
                for direction in orientations:
                    state = (row, col, direction)
                    if state not in costs:
                        costs[state] = (0, 0)
                        previous[state] = None
                        unvisited.append(state)

            end = None
            finished = set()
            while unvisited:
                best_index = 0
                for index in range(1, len(unvisited)):
                    if ((costs[unvisited[index]], unvisited[index])
                            < (costs[unvisited[best_index]], unvisited[best_index])):
                        best_index = index
                state = unvisited.pop(best_index)
                if state in finished:
                    continue
                finished.add(state)
                row, col, old_direction = state
                distance, turns = costs[state]
                if (row, col) in network and (row, col) not in connected:
                    end = state
                    break

                for direction, step in enumerate(directions):
                    neighbor_row = row + step[0]
                    neighbor_col = col + step[1]
                    if not (0 <= neighbor_row < height and 0 <= neighbor_col < width):
                        continue
                    if output[neighbor_row][neighbor_col] not in (background, color):
                        continue
                    next_state = (neighbor_row, neighbor_col, direction)
                    next_cost = (distance + 1,
                                 turns + (old_direction != -1
                                          and old_direction != direction))
                    if next_state not in costs or next_cost < costs[next_state]:
                        costs[next_state] = next_cost
                        previous[next_state] = state
                        unvisited.append(next_state)

            state = end
            while state is not None:
                row, col, direction = state
                output[row][col] = color
                network.add((row, col))
                connected.add((row, col))
                state = previous[state]

            stack = list(connected)
            while stack:
                row, col = stack.pop()
                for row_step, col_step in directions:
                    neighbor = (row + row_step, col + col_step)
                    if neighbor in network and neighbor not in connected:
                        connected.add(neighbor)
                        stack.append(neighbor)
    return output
