startNumber, endNumber = input("Enter a two number: ").split()
startNumber = int(startNumber)
endNumber = int(endNumber)

if endNumber < startNumber:
    print('The ending number must be greater than start')
else:
    for number in range(startNumber, endNumber + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=", ")
        elif number % 3 == 0:
            print("Fizz", end=", ")
        elif number % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(number, end=", ")
