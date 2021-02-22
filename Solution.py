# import importlib
from importlib import import_module as im

# Modul1 = importlib.import_module('FileFormatting')
ConverterModule = im('FileConverting')
SortModule = im('ListSorting')

inputFileName = input()
Converter = ConverterModule.Convert_To_Graph(inputFileName);
Sorter = SortModule.Sort_The_List()

sorted = Sorter.Sort(Converter.theGraph, 1, Converter.numberOfLines)

takenCourse = [[]]
numberOfTakenCourse = 0
semester = 0

'''
for i in sorted:
    print(str(i))
'''

while(numberOfTakenCourse < Converter.numberOfLines):
    semester += 1
    takenCourse.append([])
    
    ''' ambil semua matkul yang prereqnya 0 '''
    i = 0
    while(i < len(sorted)):
        if(sorted[i][1] != 0):
            i += 1
        else:       
            takenCourse[semester].append(sorted[i][0])
            sorted.pop(i)
            numberOfTakenCourse += 1
    ''' ambil semua matkul yang prereqnya 0 '''

    ''' hapus matkul yang sudah diambil dari prereq matkul lainnya '''
    for isi in takenCourse[semester]:
        for j in sorted:
            if(j[2].count(isi) > 0):
                j[2].remove(isi)
                j[1] -= 1
    ''' hapus matkul yang sudah diambil dari prereq matkul lainnya '''
    
for i in range(1, semester + 1, 1):
    print(f'Semester {i}:', end='')
    for j in takenCourse[i]:
        print(f' {j}', end='')
    print()
