def main():
    path = 'input.txt'
    content = readFile(path)
    words = formatContent(content)
    list = getMostCommonWord(words,content)
    print(list)
    writeOutput(list,content)

def readFile(path):
    file = open(path)
    content = file.readlines()
    return content

def formatContent(content):
    words=[]
    for line in content:
        line = line.strip().lower().split(" ")
        for word in line:
            L = word.strip(".,!?:;").split("'")
            for w in L:
                if w != "":
                    words.append(w)
    return words

def getMostCommonWord(words,content,nbWordsToFind=3):
    wordDict = {}
    listOfWords = []

    for word in words:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            nb = getNumberOfTextsContainingWord(word,content)
            if nb != 3:
                wordDict[word] = 1

    for x in range (nbWordsToFind):
        word = getMostOccuringWord(wordDict)
        listOfWords.append(word)
        wordDict[word] = 0
    return listOfWords

def getMostOccuringWord(wordDict):
    maxOccurence = 0
    word = None
    for key in wordDict:
        nbOccurences = wordDict[key]
        if nbOccurences >= maxOccurence:
            maxOccurence = nbOccurences
            if word != None:
                tmp = [word,key]
                tmp.sort()
                word = tmp[0]
            else:
                word = key

    return word

def getNumberOfTextsContainingWord(word,texts):
    nb = 0
    for text in texts:
        if word in text.lower():
            nb += 1
    return nb

def writeOutput(mostOccuringWord, content, filename="output.txt"):
    file = open(filename,'a')
    for word in mostOccuringWord:
        file.write(f"{getNumberOfTextsContainingWord(word,content)} {word}\n")
    file.close()
    
    

if __name__=='__main__':
    main()