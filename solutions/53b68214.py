def transform(grid):
    rows=[row[:] for row in grid];w=len(rows[0])
    def shifted(row,s):
        if s>=0:return [0]*s+row[:w-s]
        return row[-s:]+[0]*(-s)
    choice=None
    for lag in range(1,len(rows)):
        for shift in range(-w+1,w):
            if all(rows[r]==shifted(rows[r-lag],shift) for r in range(lag,len(rows))):
                choice=(lag,shift);break
        if choice:break
    lag,shift=choice
    while len(rows)<10: rows.append(shifted(rows[-lag],shift))
    return rows
