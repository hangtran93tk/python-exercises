list1 = [[1,2],[3,4]]
list2 = [[1,2,3],[4,5,6],[7,8,9]]

def get_flat_list(list):
    new_list = []
    for i in range(len(list)):
       new_list += list[i] if i % 2 == 0 else list[i][::-1]
    return new_list

new_list = get_flat_list(list2)
print(new_list)

