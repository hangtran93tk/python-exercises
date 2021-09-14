tuple1 = ((1,2,3,4),(3,5,2,1),(2,2,3,1))

def sum_row_elements(tuple):
    sum_list = []
    sum_row = 0
    j = 0
    for i in range(len(tuple)):
        print(tuple[i][i:])

sum_row_elements(tuple1)
