import SomeModules as m
import random

hang = int(m.nhapSo("Nhap so hang"))
cot = int(m.nhapSo("Nhap so cot"))

def findMatrix(hang, cot):
    matrix = []
    for i in range(hang):
        matrix.append([])
        for j in range(cot):
            matrix[i].append(random.randint(0,9))
    return matrix

matrix = findMatrix(hang, cot)
print(matrix)
