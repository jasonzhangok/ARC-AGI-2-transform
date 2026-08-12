def transform(grid):
    """Return the source pattern of a larger, possibly boundary-clipped 2x copy."""
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row: counts[value]=counts.get(value,0)+1
    background=None
    for value in counts:
        if background is None or counts[value]>counts[background]:background=value
    colors = [color for color in counts if color != background]

    boxes={};masks={}
    for color in colors:
        points=[(row,column) for row,values in enumerate(grid) for column,value in enumerate(values) if value==color]
        box=(min(row for row,_ in points),max(row for row,_ in points),min(column for _,column in points),max(column for _,column in points))
        boxes[color]=box;top,bottom,left,right=box
        masks[color]=[[int(grid[row][column]==color) for column in range(left,right+1)] for row in range(top,bottom+1)]

    sources = []
    for source in colors:
        doubled=[]
        for mask_row in masks[source]:
            doubled_row=[value for value in mask_row for _ in range(2)];doubled.extend([doubled_row[:],doubled_row[:]])
        for larger_copy in colors:
            if larger_copy == source or counts[larger_copy] <= counts[source]:
                continue
            top, bottom, left, right = boxes[larger_copy]
            if not (
                top == 0
                or bottom == height - 1
                or left == 0
                or right == width - 1
            ):
                continue
            part=masks[larger_copy];whole_height,whole_width=len(doubled),len(doubled[0]);part_height,part_width=len(part),len(part[0])
            contains=(part_height<=whole_height and part_width<=whole_width and any(all(part[row][column]==doubled[placement_top+row][placement_left+column] for row in range(part_height) for column in range(part_width)) for placement_top in range(whole_height-part_height+1) for placement_left in range(whole_width-part_width+1)))
            if contains:
                sources.append(source)
                break

    if len(sources) != 1:
        raise ValueError("expected exactly one object with a clipped doubled copy")

    top, bottom, left, right = boxes[sources[0]]
    output=[row[left:right+1] for row in grid[top:bottom+1]]
    return output
