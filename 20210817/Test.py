# i = 0
# while i <= 10:
#     i += 1
#     print (i)
#     if i % 2 == 0:
#         continue

i = 0

j = 20

while True:

    j -= 2

    i += 3

    if i >= j:

        break

    if j > 15:

        continue

    print(i, j, sep='', end='')

else:

    print(j, end='')

print('a')