def transform(grid):
    marker=next(r for r,row in enumerate(grid) if row[0]==2)
    body=[row[1:] for row in grid];start=(-marker)%len(body)
    output = body[start:]+body[:start]
    return output
