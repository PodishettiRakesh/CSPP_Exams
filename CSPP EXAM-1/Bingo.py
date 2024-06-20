import random
def empty_Grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(None)
        grid.append(row)
    return grid
# rows = 5
# cols = 5
# print(empty_Grid(rows, cols))
