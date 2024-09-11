def main():
    path = 'input.txt'
    string,subString = readFile(path)
    found, length = isSubString(string,subString)
    writeOutput(found,length)

def readFile(path):
    file = open(path)
    subString = file.readline().strip("\n")
    string = file.readline()
    return string,subString

def isSubString(string,subString):
    indexString, indexSubString = 0, 0
    
    while indexSubString<len(subString) and indexString<len(string):
        if subString[indexSubString] == string[indexString]:
            indexSubString += 1
        indexString +=1
    found = indexSubString == len(subString)
    return found, indexSubString

def writeOutput(found,length,fileName = 'output.txt'):
    file = open(fileName,'a')
    if found:
        file.write(f"OK")
    else:
        file.write(f"NOK {length}") 


if __name__=="__main__":
    main()