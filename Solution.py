import os
import csv
# import importlib
from importlib import import_module as im
import math

# Modul1 = importlib.import_module('FileFormatting')
Modul1 = im('FileFormatting')
CTG = Modul1.Convert_To_Graph('matkul.txt');

print(CTG.theGraph)
print(CTG.courseCodes)

for i in range(CTG.numberOfLines):
    print(str(CTG.courseCodes[i]) + ' ' + str(CTG.theGraph[i]))
