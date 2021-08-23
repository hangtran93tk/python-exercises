# import random
#
# randomNumber = random.randint(1,10)
# # chooseNumber = int(input("Hay nhap mot so tu nhien 1-10 : "))
# falseRound = 0
# while falseRound < 3:
#     chooseNumber = int(input("Hay nhap mot so tu nhien 1-10 : "))
#     print(f"So ngau nhien la : {randomNumber}")
#     # for i in range(2):
#     print(f"So ban da nhap {chooseNumber}")
#     if randomNumber == chooseNumber:
#         print("Chuc mung ban da doan dung")
#         print(f"So ngau nhien la : {randomNumber}")
#         exit()
#     elif randomNumber > chooseNumber:
#         print("So ban nhap be hon so random")
#         falseRound += 1
#     else:
#         print("So ban nhap lon hon so random")
#         # chooseNumber = int(input("Hay nhap mot so tu nhien 1-10 : "))
#         falseRound += 1
#
# print("Rat tiec ban da het so luot")
# print(f"So ngau nhien la : {randomNumber}")

import random

randomNumber = random.randint(1,10)

for i in range(3):
    chooseNumber = int(input("Hay nhap mot so tu nhien 1-10 : "))
    print(f"So ban da nhap {chooseNumber}")
    if randomNumber == chooseNumber:
        print("Chuc mung ban da doan dung")
        print(f"So ngau nhien la : {randomNumber}")
        break
    elif randomNumber > chooseNumber:
        print("So ban nhap be hon so random")
    else:
        print("So ban nhap lon hon so random")
else:
    print("Rat tiec ban da het so luot")
    print(f"So ngau nhien la : {randomNumber}")