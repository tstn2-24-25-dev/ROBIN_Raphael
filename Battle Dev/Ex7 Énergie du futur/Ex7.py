def main():
    path = 'input.txt'
    energyProduction = readFile(path=path)
    futureEnergy = computeFutureEnergy(energyProduction, 4)
    writeOutput(futureEnergy)

def readFile(path):
    file = open(path)
    energyProduction = int(file.readline().strip())
    return energyProduction

def computeFutureEnergy(energyProduction,years):
    for x in range(years):
        if energyProduction%3 == 0:
            energyProduction = energyProduction // 3
        elif energyProduction%2 == 0:
            energyProduction = energyProduction // 2
        else:
            energyProduction = energyProduction - 1
    return energyProduction

def writeOutput(energy,path='output.txt'):
    file = open(path,'a')
    file.write(str(energy))
    file.close

if __name__=="__main__":
    main()