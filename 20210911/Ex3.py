list1 = [[1,2],[3,4]]
list2 = [[1,2,3],[3,4,5],[6,7,8]]

def sum_diagonal(list):
    sum = 0
    if len(list) == len(list[0]):
        for i in range(len(list)):
            sum += list[i][i]
    return sum

sum = sum_diagonal(list2)
print(sum)