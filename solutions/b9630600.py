def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    boxes = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 3 and (row, col) not in seen:
                stack = [(row, col)]
                seen.add((row, col))
                top = bottom = row
                left = right = col
                while stack:
                    current_row, current_col = stack.pop()
                    top = min(top, current_row)
                    bottom = max(bottom, current_row)
                    left = min(left, current_col)
                    right = max(right, current_col)
                    for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = current_row + delta_row
                        next_col = current_col + delta_col
                        if (0 <= next_row < height and 0 <= next_col < width
                                and grid[next_row][next_col] == 3
                                and (next_row, next_col) not in seen):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                boxes.append((top, left, bottom, right))

    additions = set()
    removals = set()
    for first_index in range(len(boxes)):
        for second_index in range(first_index + 1, len(boxes)):
            first = boxes[first_index]
            second = boxes[second_index]

            if first[1] < second[1]:
                left_box, right_box = first, second
            else:
                left_box, right_box = second, first
            overlap_start = max(left_box[0], right_box[0])
            overlap_end = min(left_box[2], right_box[2])
            overlap = overlap_end - overlap_start + 1
            gap = right_box[1] - left_box[3] - 1
            blocked = False
            if gap >= 1 and overlap >= 3 and gap <= overlap:
                for other_index in range(len(boxes)):
                    if other_index != first_index and other_index != second_index:
                        other = boxes[other_index]
                        common_start = max(overlap_start, other[0])
                        common_end = min(overlap_end, other[2])
                        if (left_box[3] < other[1] and other[3] < right_box[1]
                                and common_start <= common_end):
                            blocked = True
                if not blocked:
                    for bridge_row in {overlap_start + 1, overlap_end - 1}:
                        for bridge_col in range(left_box[3] + 1, right_box[1]):
                            additions.add((bridge_row, bridge_col))
                    for middle_row in range(overlap_start + 2, overlap_end - 1):
                        removals.add((middle_row, left_box[3]))
                        removals.add((middle_row, right_box[1]))

            if first[0] < second[0]:
                top_box, bottom_box = first, second
            else:
                top_box, bottom_box = second, first
            overlap_start = max(top_box[1], bottom_box[1])
            overlap_end = min(top_box[3], bottom_box[3])
            overlap = overlap_end - overlap_start + 1
            gap = bottom_box[0] - top_box[2] - 1
            blocked = False
            if gap >= 1 and overlap >= 3 and gap <= overlap:
                for other_index in range(len(boxes)):
                    if other_index != first_index and other_index != second_index:
                        other = boxes[other_index]
                        common_start = max(overlap_start, other[1])
                        common_end = min(overlap_end, other[3])
                        if (top_box[2] < other[0] and other[2] < bottom_box[0]
                                and common_start <= common_end):
                            blocked = True
                if not blocked:
                    for bridge_col in {overlap_start + 1, overlap_end - 1}:
                        for bridge_row in range(top_box[2] + 1, bottom_box[0]):
                            additions.add((bridge_row, bridge_col))
                    for middle_col in range(overlap_start + 2, overlap_end - 1):
                        removals.add((top_box[2], middle_col))
                        removals.add((bottom_box[0], middle_col))

    result = [row[:] for row in grid]
    for row, col in removals:
        result[row][col] = 0
    for row, col in additions:
        result[row][col] = 3
    return result
