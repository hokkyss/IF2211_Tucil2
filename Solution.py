import os
import csv
import invoke
# import importlib
from importlib import import_module as im
import math

# Modul1 = importlib.import_module('FileFormatting')
Modul1 = im('FileConverting')
CTG = Modul1.Convert_To_Graph('matkul.txt');

print(CTG.theGraph)
# print(CTG.courseCodes)

for i in range(CTG.numberOfLines):
    print(str(CTG.theGraph[i]))

