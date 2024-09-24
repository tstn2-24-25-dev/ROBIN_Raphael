import time
def main():
    path = "input.txt"
    visual = True
    displaySpeed = 1
    nbRectangles, rectangles = readFile(path)
    setOfCells = set()
    setupBoard(nbRectangles,rectangles,setOfCells)
    board,generation = game(setOfCells,visual,displaySpeed)
    writeOutput(generation)

def readFile(path):
    file = open(path)
    nbRectangles = file.readline()
    rectangles = file.readlines()
    return nbRectangles,rectangles

def formatRectangle(rectangle):
    rectangle = rectangle.split(' ')
    for i in range (len(rectangle)):
        rectangle[i]=int(rectangle[i])
    return rectangle

def addCellsFromRectangle(rectangle,setOfCells):
    x1,y1,x2,y2 = rectangle
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            cell = (x,y)
            setOfCells.add(cell)

def setupBoard(nbRectangles,rectangles,setOfCells):
    for n in range(int(nbRectangles)):
        rectangle = formatRectangle(rectangles[n])
        addCellsFromRectangle(rectangle,setOfCells)

def computeNextGeneration(setOfCells, nextGeneration):
    for cell in setOfCells:
        x,y = cell

        if (x-1,y+1) in setOfCells:
            newCell = (x,y+1)
            nextGeneration.add(newCell)

        if (x,y-1) in setOfCells:
            if (x-1,y) not in setOfCells:
                nextGeneration.add(cell)
        else:
            if (x-1,y) in setOfCells:
                nextGeneration.add(cell)

def game(setOfCells,visual=False,speed = 1):
    generation = 0
    while len(setOfCells)!=0:
        generation += 1
        if visual:
            print(f"Generation {generation}, number of living cells: {len(setOfCells)}")    
            displayBoard(setOfCells)
            time.sleep(speed)
        nextGeneration = set()
        computeNextGeneration(setOfCells,nextGeneration)
        setOfCells = nextGeneration
    
    if visual:
        print(f"Generation {generation+1}, number of living cells: {len(setOfCells)}")    
        displayBoard(setOfCells)
        time.sleep(speed)

    return setOfCells, generation

def writeOutput(generation,fileName='output.txt'):
    file = open(fileName,'a')
    file.write(str(generation))
    file.close()

def displayBoard(set):
    maxX,maxY = 10,10
    for cell in set:
        x,y = cell
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

    board = []
    for x in range(maxX+1):
        board.append([])
        for y in range (maxY+1):
            board[x].append(' ')
    #printBoard(board)
    
    for cell in set:
        x,y=cell
        #print(f"{x-minX} {y-minY}")
        board[x][y] = "O"
    printBoard(board)
            
def printBoard(board):
    
    for line in board:
        string = ""
        for cell in line:
            string += cell +" "
        print(string)
    print()

if __name__=="__main__":
    main()