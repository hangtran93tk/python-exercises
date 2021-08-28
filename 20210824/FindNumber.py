import SomeModule as module

num = int(module.nhapSo("so n"))
count = 0
a = [0]
tailA = len(a) - 1
lastNum = a[tailA]
addNum = a[tailA] + 1

for i in range(len((str(addNum)))):
    count = str(lastNum).find(str(addNum)[i])



