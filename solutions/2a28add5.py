def transform(grid):
    result = []
    for row in grid:
        transformed = [7] * len(row)
        if 6 in row:
            anchor = row.index(6)
            left_count = sum(value != 7 for value in row[:anchor])
            right_count = sum(value != 7 for value in row[anchor + 1:])
            transformed[anchor - left_count:anchor + right_count + 1] = [8] * (left_count + right_count + 1)
        result.append(transformed)
    output = result
    return output
