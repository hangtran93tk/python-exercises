tuple1 = ((1,2,3,4),(3,5,2,1),(2,2,3,1))

def sum_row_elements(tuple):
    new_list = []
    column_sum = 0
    for i in range(len(tuple[0])):
        for j in range(len(tuple)):
            column_sum += tuple[j][i]
        new_list.append(column_sum)
        column_sum = 0
    return new_list

new_tuple = tuple(sum_row_elements(tuple1))
print(new_tuple)
