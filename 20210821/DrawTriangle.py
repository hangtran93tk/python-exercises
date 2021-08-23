char = "*"
noChar = " "
for i in range(6):
    print(char * i, end="\n")

print("\n")
for i in range(5,0,-1):
    print(char * i, end="\n")

print("\n")
for i in range(5,0,-1):
    print(i*" " + "*"*(6-i) )

print("\n")
for i in range(5,0,-1):
    print(i*"*" + " "*(6 -i))
