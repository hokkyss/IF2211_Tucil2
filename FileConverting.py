import csv

class Convert_To_Graph:
    theGraph = [];
    courseByID = [];
    numberOfLines = 0;
    def __init__(self, inputFileName):
        # perlihatkan isi file
        self.printFileContent(inputFileName)
        # tahap pertama langkah 2.
        self.formattingFile('test/' + inputFileName, 'outputFile.txt')
        # tahap pertama langkah 3.
        self.theGraph = self.takeFormattedFile('outputFile.txt')
        # tahap pertana langkah 5.
        self.theGraph = self.intoAdjacencyList()
        # tahap pertama langkah 6.
        self.theGraph = self.intoCourseAndPrereq()

    def printFileContent(self, inputFileName):
        inputFile = open('test/' + str(inputFileName))
        for i in inputFile:
            print(i, end = '')
        inputFile.close()
        
    def formattingFile(self, inputFileName, outputFileName):
        inputFile = open(str(inputFileName))
        fileContent = csv.reader(inputFile, delimiter = ",")
        list = []

        for row in fileContent:
            content = f'{"".join(row)}'
            contentLength = len(content)
            list.append(content[:contentLength - 1])

        outputFile = open(outputFileName, 'w')
        for row in list:
            outputFile.write(row + '\n')

        outputFile.close()
        inputFile.close()
        return

    def takeFormattedFile(self, outputFileName):
        outputFile = open(outputFileName, 'r')

        isifile = csv.reader(outputFile, delimiter = ' ')
        complete = []
        for row in isifile:
            complete.append([])
            for kolom in row:
                complete[self.numberOfLines].append(kolom)
            self.numberOfLines += 1
            
        return complete

    def intoAdjacencyList(self):
        temporaryGraph = []
        for i in range(0, self.numberOfLines, 1):
            self.courseByID.append(self.theGraph[i][0])
            temporaryGraph.append([])
            for j in range(1, len(self.theGraph[i]), 1):
                temporaryGraph[i].append(self.theGraph[i][j])
                      
        return temporaryGraph

    def intoCourseAndPrereq(self):
        temporaryGraph = []
        for i in range(0, self.numberOfLines, 1):
            temporaryGraph.append([self.courseByID[i], len(self.theGraph[i]), self.theGraph[i]])
        return temporaryGraph
