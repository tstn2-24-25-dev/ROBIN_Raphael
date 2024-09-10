def main():
    path = 'inventaire.txt'
    firstLine,content = readFile(path=path)
    numberOfArticles = int(firstLine.strip())
    formattedContent = formatContent(content=content)
    dictValues,dictCount = buildDictionaries(formattedContent)
    dictInventory = computeValues(dictCount=dictCount, dictValues=dictValues)
    highestValueItem,value = findHighestValueItem(dictInventory=dictInventory)
    createOutputFile(highestValueItem)


def readFile(path): 
    file = open(path)
    firstLine = file.readline()
    content = file.readlines()
    file.close()
    return (firstLine,content)

def formatContent(content):
    formattedContent = []
    for line in content:
        formattedContent.append(line.split(' '))
    return formattedContent

def buildDictionaries(content):
    dictionaryofValues={}
    dictionaryofCount={}
    for line in content:
        itemName, value = line[0],line[1]
        dictionaryofValues[itemName]=int(value)
        if itemName not in dictionaryofCount.keys():
            dictionaryofCount[itemName]=1
        else:
            dictionaryofCount[itemName]=dictionaryofCount[itemName]+1 
    return dictionaryofValues,dictionaryofCount

def computeValues(dictValues,dictCount):
    dictInventory = {}
    for item in dictCount:
        dictInventory[item] = dictValues[item] * dictCount[item]
    return dictInventory

def findHighestValueItem(dictInventory):
    maxValue = 0
    maxValueItem = ""
    for item in dictInventory:
        if dictInventory[item]>maxValue:
            maxValue = dictInventory[item]
            maxValueItem = item
    return maxValueItem,maxValue
 
def createOutputFile(item, fileName = "outputInventaire.txt"):
    file = open (fileName,'a')
    file.write(item)

if __name__ =="__main__":
    main()