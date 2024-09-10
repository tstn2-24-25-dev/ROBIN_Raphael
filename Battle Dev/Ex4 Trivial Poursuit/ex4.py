def main():
    
    tileColors=["violet", "orange", "jaune", "vert", "rose", "bleu"]
    fileName  = 'input.txt'
    content = readFile(fileName)
    distance = computeTotalDistance(content=content)
    color = computeColor(distance,tileColors)
    writeOutput(color)



def readFile(fileName):
    file = open (fileName)
    content =  file.readlines()
    file.close()
    return content

def computeTotalDistance(content):
    distance = 0
    for line in content:
        distance += int(line.strip())
    return distance

def computeColor(distance,tileColors):
    return tileColors[distance%len(tileColors)]

def writeOutput(color,fileName ="output.txt"):
    file = open(fileName,'a')
    file.write(color)
    file.close()

if __name__ == '__main__':
    main()