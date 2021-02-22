import os
# import nltk
import csv
import importlib
import math

# from nltk.stem import PorterStemmer

location = os.getcwd();

class Convert_To_Graph:
    theGraph = [];
    numberOfLines = 0;
    def __init__(self, inputFileName):
        self.formattingFile(inputFileName, 'outputFile.txt')
        self.theGraph = self.takeFormattedFile('outputFile.txt')
        self.theGraph = self.intoAdjacencyList()
    ''' FOR TESTING PURPOSE
    def Testing(self):
        print('AAAAAA')
        return
    FOR TESTING PURPOSE '''

    def formattingFile(self, inputFileName, outputFileName):
        inputFile = open(str(inputFileName))

        isifile = csv.reader(inputFile, delimiter = ",")
        list = []
        
        for row in isifile:
            isi = f'{"".join(row)}'
            lenisi = len(isi)
            list.append(isi[:lenisi - 1])

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
                complete[self.numberOfLines].append(int(kolom))
            self.numberOfLines += 1
            
        return complete

    def intoAdjacencyList(self):
        temporaryGraph = []
        for i in range(0, self.numberOfLines, 1):
            temporaryGraph.append([])
            for j in range(1, len(self.theGraph[i]), 1):
                temporaryGraph[i].append(self.theGraph[i][j])
                      
        return temporaryGraph
