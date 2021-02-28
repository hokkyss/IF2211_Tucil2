from importlib import import_module as im

ConverterModule = im('13519143-FileConverting')
# SortModule = im('13519143-ListSorting')

inputFileName = input('Masukkan nama file : ')
Converter = ConverterModule.Convert_To_Graph(inputFileName);
# Sorter = SortModule.Sort_The_List()

takenCourse = [[]]
numberOfTakenCourse = 0
semester = 0
myGraph = Converter.theGraph

while(numberOfTakenCourse < Converter.numberOfLines):
    semester += 1
    takenCourse.append([])
    
    ''' ambil semua matkul yang prereqnya 0 '''
    i = 0
    while(i < len(myGraph)):
        if(myGraph[i][1] != 0):
            i += 1
        else:       
            takenCourse[semester].append(myGraph[i][0])  # kode mata kuliahnya
            myGraph.pop(i)
            numberOfTakenCourse += 1
    ''' ambil semua matkul yang prereqnya 0 '''

    ''' hapus matkul yang sudah diambil dari prereq matkul lainnya '''
    for matkulDiambil in takenCourse[semester]:
        for j in myGraph:
            if(j[2].count(matkulDiambil) > 0):
                j[2].remove(matkulDiambil)
                j[1] -= 1
    ''' hapus matkul yang sudah diambil dari prereq matkul lainnya '''

for i in range(1, semester + 1, 1):
    print(f'Semester {i}:', end='')
    for matkul in takenCourse[i]:
        print(f' {matkul}', end='')
    print()
