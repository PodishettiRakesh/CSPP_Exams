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


def generateComputerNumbers():
    return random.sample(range(1,25),16)


def display_Grid(grid):
    for r in grid:
        for n in r:
            if n is not None:
                print('n',end=' ')
            else:
                print('.',end=' ')
        print()
    print()


def markNumber(grid, number):
    for i in range(5):
        for j in range(5):
            if grid[i][j]==number:
                grid[i][j]='x'
    return grid

def checkWinner(grid):
    for row in grid:
        for each in row:
            if each is not None and each != 'x':
                return False
    return True