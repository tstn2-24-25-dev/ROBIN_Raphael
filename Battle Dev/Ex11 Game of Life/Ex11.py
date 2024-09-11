def main():
    path = "input.txt"
    nbRectangles, rectangles = readFile(path)
    setOfCells = set()
    setupBoard(nbRectangles,rectangles,setOfCells)
    print(setOfCells)

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
            print(cell)
            setOfCells.add(cell)

def setupBoard(nbRectangles,rectangles,setOfCells):
    for n in range(int(nbRectangles)):
        rectangle = formatRectangle(rectangles[n])
        addCellsFromRectangle(rectangle,setOfCells)



if __name__=="__main__":
    main()