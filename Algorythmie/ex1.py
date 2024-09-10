def main():
    path = 'text.txt'
    firstLine, content = readFile(path)
    firstLineFormated = formatFirstLine(firstLine)
    assignValues(firstLineFormated)
    scores = assignScores(content)
    wordsSortedByScore = sortWordsByScore(scores)
    creatOutputFile(wordsSortedByScore)

values = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
 }

def readFile(path): 
    with open(path, ) as file:
        firstLine = file.readline()
        content = file.readlines()
    return (firstLine,content)

def formatFirstLine(line):
    return (line.split(' '))

def assignValues(line):
    for i in range(0,len(line),2):
        values[line[i]]=line[i+1]

def computeScore(word):
    score = 0
    for char in word:
        score += int(values[char])
    return score

def assignScores(content):
    scores = []
    for line in content:
        word = line.strip()
        wordAndScore = (word,computeScore(word))
        scores.append(wordAndScore)
    return scores
    
def sortWordsByScore(scores): #swap sort
    index = 1
    output=[]
    for minIndex in range(len(scores)):
        indexMax = minIndex
        for index in range(minIndex,len(scores)):
            if scores[indexMax][1]<scores[index][1]:
                scores[index],scores[indexMax]=scores[indexMax],scores[index] 
        output.append(scores[indexMax])
    return output

def creatOutputFile(sortedWords):
    file = open("output.txt",'a')
    lines = []
    for word in sortedWords:
        lines.append(f"{word[0]}\r")
    file.writelines(lines)
    file.close()
    

if __name__ =="__main__":
    main()