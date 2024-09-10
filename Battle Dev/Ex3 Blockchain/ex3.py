def main():
    fileName = "input.txt"
    numberOfHosts, modificationRequests, content = readFile(fileName=fileName)
    #print(f"{numberOfHosts},{modificationRequests},{content}")
    formattedContent = formatContent(content=content)
    #print(formattedContent)
    filteredChanges = discardUnpopularChanges(formattedContent,numberOfHosts)
    writeOutput(filteredChanges)

def readFile(fileName):
    file = open(file=fileName)
    numberOfHosts = int(file.readline())
    modificationRequests = int(file.readline())
    content = file.readlines()
    return numberOfHosts, modificationRequests, content

def formatContent(content):
    formattedContent=[]
    for line in content:
        formattedContent.append(line.strip().split(' '))
    return formattedContent

def discardUnpopularChanges (formattedContent, numberOfHosts):
    filteredContent = []
    for change in formattedContent:
        if int(change[1])>=numberOfHosts/2:
            filteredContent.append(change[0])
    return filteredContent

def writeOutput(filteredChanges,fileName = 'output.txt'):
    file = open(fileName,'a')
    for change in filteredChanges:
        file.write(change)


if __name__ =="__main__":
    main()