import random
def emptyGrid(rows,cols):
    grid=[]
    for i in range(rows):
        s=[]
        for j in range(cols):
            s.append("_")
        grid.append(s)
    return grid
# print(emptyGrid(5,5))


# print(numbers)
def populateGrid(grid,numbers):
    count=0
    while count<16:
        row= random.choice([0,1,2,3,4])
        col=random.choice([0,1,2,3,4])
        if grid[row][col]=="_":
            grid[row][col]=numbers.pop()
            count+=1
    return grid
# numbers=random.sample(range(1,25),16)
# grid=emptyGrid(5,5)
# print(populateGrid(grid,numbers))

def getUserNumber():
    while True:
        try:
            num=int(input("enter your number between 1 to 16: "))
            if 1<=num<=25:
                return num
        except ValueError:
            print("invalid inputs")
def generateComputerNumber():
    num=random.sample(range(1,16),1)
    return num[0]


def displayGrid(grid):
    for row in grid:
        for each in row:
            if each!="_":
                print(each,end="  ")
            else:
                print("*",end="  ")
        print()

