import math

def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True;

numList = [-10,5,2,8,7,13,121]
numAfterCheck = []

for num in numList:
    if isPrimeNumber(num):
        numAfterCheck.append(num)
print(numAfterCheck)