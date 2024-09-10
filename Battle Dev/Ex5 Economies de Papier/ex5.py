def main():
    fileName = "input4.txt"
    pageSize = 10
    content = readInput(fileName)
    formattedContent = formatContent(content)
    numberOfPages = computeNumberOfPages(formattedContent,pageSize,True)
    writeOutput(numberOfPages)

def readInput(fileName):
    file = open(fileName)
    content = file.readline()
    file.close()
    return content

def formatContent(content):
    formattedContent = content.strip().split(' ')
    return formattedContent

def computeNumberOfPages(formattedContent,pageSize,verbose=False):
    sizeRemaining = pageSize
    numberOfPages = 1
    index = 0
    while index<len(formattedContent):
        imageSize = int(formattedContent[index])
        if verbose:
            print(f"imageSize: {imageSize}; sizeRemaining: {sizeRemaining}; numberOfPages: {numberOfPages}")
        if imageSize > sizeRemaining:
            if verbose:
                print("insufficient space, new page needed")
            numberOfPages += 1
            sizeRemaining = pageSize - imageSize
        else:
            sizeRemaining -= imageSize
        index += 1
    if verbose:
        print(f"total pages needed: {numberOfPages}")
    return numberOfPages

def writeOutput(numberOfPages,fileName = 'output.txt'):
    file = open(fileName,'a')
    file.write(str(numberOfPages))
    file.close()


if __name__ == '__main__':
    main()