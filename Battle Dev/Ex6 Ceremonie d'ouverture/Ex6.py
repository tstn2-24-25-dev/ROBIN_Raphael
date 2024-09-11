def main():
    path = "input.txt"
    content = readFile(path)
    lines = formatContent(content)
    country,time = getHighestTime(lines)
    writeOutput(country)

def readFile(path):
    file = open(path)
    file.readline()
    content = file.readlines()
    return content

def formatContent(content):
    lines =[]
    for line in content:
        lines.append(line.strip().split(' '))
    return lines

def computeTimeToArrival(distance,speed):
    return distance/speed

def getHighestTime(lines):
    maxTime=0
    maxTimeCountry = ""
    for line in lines:
        country, distance, speed = line
        time = computeTimeToArrival(int(distance),int(speed))
        if time > maxTime:
            maxTime = time
            maxTimeCountry = country
    return maxTimeCountry,maxTime

def writeOutput(country,fileName='output.txt'):
    file = open(fileName,'a')
    file.write(country)
    file.close()

if __name__ == "__main__":
    main()