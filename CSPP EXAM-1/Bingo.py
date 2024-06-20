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


def populate_grid(grid, numbers):
    x = set()
    for num in numbers:
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if (row, col) not in x:
                grid[row][col] = num
                x.add((row, col))
                break
    return grid

def getUserNumbers():
    user_numbers = []
    while len(user_numbers) < 16:
        try:
            num = int(input(f"Enter number {len(user_numbers) + 1}/16 (between 1 and 25): "))
            if num < 1 or num > 25:
                print("number is not valid.")
            elif num in user_numbers:
                print("number already chosen.")
            else:
                user_numbers.append(num)
        except ValueError:
            print("Invalid input.")
    return user_numbers
# getUserNumbers()