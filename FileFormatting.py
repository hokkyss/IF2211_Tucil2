import os
# import nltk
import csv
import importlib
import math

# from nltk.stem import PorterStemmer

location = os.getcwd();

class Convert_To_Graph:
    graf = 0;
    def __init__(self, inputFileName):
        self.formattingFile(inputFileName, 'outputFile.txt')
        self.graf = self.takeFormattedFile()
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

    def takeFormattedFile(self):
        outputFile = open('outputFile.txt', 'r')

        isifile = csv.reader(outputFile, delimiter = ' ')
        complete = []
        baris = 0
        for row in isifile:
            complete.append([])
            for kolom in row:
                complete[baris].append(int(kolom))
            baris += 1
            
        return complete
        
