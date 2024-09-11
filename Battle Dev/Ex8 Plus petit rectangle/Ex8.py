def main():
    path = 'input.txt'
    content = readFile(path)
    lines = formatContent(content)
    rectangle = findSmallestRectangle(lines=lines)
    writeOutput(rectangle)

def readFile(path):
    file = open(path)
    content =[]
    numberOfLines = int(file.readline())
    for x in range(numberOfLines):
        content.append(file.readline()) 
    return content

def formatContent(content):
    lines=[]
    for line in content:
        lines.append(line.strip().split(' '))
    return lines

def computeRectangleArea(x1,y1,x2,y2):
    height = abs(int(x2)-int(x1))
    width = abs(int(y2)-int(y1))
    return height*width

def findSmallestRectangle(lines):
    smallestArea = float('inf')
    smallestRectangle = (0,0,0,0)
    for line in lines:
        x1,y1,x2,y2 = line
        rectangle =x1,y1,x2,y2
        area = computeRectangleArea(x1,y1,x2,y2)
        if area < smallestArea:
            smallestArea = area
            smallestRectangle = rectangle
    return smallestRectangle

def formatOutput(rectangle):
    x1,y1,x2,y2 = rectangle
    if int(x1)>int(x2):
        xMin, xMax = x2, x1
    else:
        xMin, xMax = x1, x2
    if int(y1)>int(y2):
        yMin, yMax = y2, y1
    else:
        yMin, yMax = y1, y2
        
    return f"{xMin} {yMin} {xMin} {yMax} {xMax} {yMin} {xMax} {yMax}"

def writeOutput(rectangle,fileName='output.txt'):
    file = open(fileName,'a')
    file.write (formatOutput(rectangle))
    file.close()

if __name__=='__main__':
    main()