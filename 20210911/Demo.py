friends = ("Tran", "Hoang", "Pham", "Nguyen")
friends2 = ("Tran",)
#Slicing [start : stop : step]
print(friends[-2:])
print(friends[-3:-1])
print(type(friends))

#Unpack
a,b, *c = friends
*a, b, c = friends
#print(a,b)
print(b)

#Xoa : Doi sang List -> add OR del -> doi sang Tuple
friends += friends2
print(friends)