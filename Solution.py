# import importlib
from importlib import import_module as im
import math

# Modul1 = importlib.import_module('FileFormatting')
ConverterModule = im('FileConverting')
SortModule = im('ListSorting')
Converter = ConverterModule.Convert_To_Graph('matkul.txt');
Sorter = SortModule.Sort_The_List()

# print(Converter.theGraph)
# print(CTG.courseCodes)

for i in range(Converter.numberOfLines):
    print(str(Converter.theGraph[i]))

hasil = Sorter.Sort(Converter.theGraph, 1, Converter.numberOfLines)
for i in range(Converter.numberOfLines):
    print(str(hasil[i]))
