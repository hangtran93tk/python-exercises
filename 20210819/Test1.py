# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# Tuple
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x, end=", ")
#
# for x in (1, 10, 3):
#   print(x, end=", ")

# for x in range(1,6):
#   for y in  range(1,6):
#     print(x,y)

a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
sum = 0

for i in  range (a, b + 1):
    sum += i

print(f"Tong tu {a} toi {b} la {sum}")
