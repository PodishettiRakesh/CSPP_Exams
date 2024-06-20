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

def userTurn(user_grid,computer_grid,number):
    for i in range(len(user_grid)):
        for j in range(len(user_grid[0])):
            if user_grid[i][j]==number:
                print("hello")
                print(user_grid[i][j])
                user_grid[i][j]="x"

    for i in range(len(computer_grid)):
        for j in range(len(computer_grid[0])):
            if computer_grid[i][j]==number:
                print("hello")
                print(computer_grid[i][j])
                computer_grid[i][j]="x"
    return user_grid,computer_grid


def computerTurn(user_grid,computer_grid):
    number=0
    while True:
        row=random.choice([0,1,2,3,4])
        col=random.choice([0,1,2,3,4])
        if computer_grid[row][col]!="_" and computer_grid[row][col]!="x":
            number+=computer_grid[row][col]
            computer_grid[row][col]="x"
            break
    print(number,"number")
    for i in range(len(user_grid)):
        for j in range(len(user_grid[0])):
            if user_grid[i][j]==number:
                user_grid[i][j]="x"
    return user_grid,computer_grid 



def checkWinner(grid):
    for row in grid:
        for each in row:
            # print(each)
            if each!="_" and each!="x":
                return False
    return True


def main():
    print("welcome to the bingo multiplayer game")
    grid1=emptyGrid(5,5)
    grid2=emptyGrid(5,5)
    count=0
    user_numbers=[]
    while count<16:
        print(f"your numbers:{user_numbers}")
        try:
            num=int(input("enter your unique number between 1 and 25: "))
            if num not in user_numbers or 1>=num<=25:
                user_numbers.append(num)
                count+=1
            else:
                print("number already present , please find unique or check number between  1 and 25 ")
        except ValueError:
            print("invalid inputs")
    # user_numbers=[1,2,3,5,6,7,12,13,14,15,18,19,20,21,22,23]
    comp_numbers=[1,2,3,6,7,12,8,13,14,15,18,19,20,21,22,23]
    # comp_reaming_nums=[1,2,3,6,7,12,8,13,14,15,18,19,20,21,22,23]

    user_grid=populateGrid(grid1,user_numbers)
    compu_grid=populateGrid(grid2,comp_numbers)

    currentPlayer=0
    player=["your","computer"]
    while True:
        print("your current board")
        displayGrid(user_grid)
        print("computer current baord")
        displayGrid(compu_grid)
        print(f"{player[currentPlayer]} turn now")
        if currentPlayer==0:
            number=getUserNumber()
            user_grid,compu_grid=userTurn(user_grid,compu_grid,number)
        if currentPlayer==1:
            user_grid,compu_grid=computerTurn(user_grid,compu_grid)
        if checkWinner(user_grid):
            return f"your the winner"
        
        if checkWinner(compu_grid):
            return f"computer is winner"
        else:
            currentPlayer=1-currentPlayer
        

print(main())
