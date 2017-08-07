def printFile(FileName):
    with open(FileName, encoding='UTF-8') as inFile:
        for line in inFile:
            print(line)
printFile("data/temp/najib.txt")

