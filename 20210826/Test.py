# def sum(start, end):
#     global total
#     for i in range(start, end + 1):
#         total += i
#
# total = 55
# sum(1,10)
# print(total)

# def plus(a,b):
#     return a + b
#
# def multi(a,b):
#     return a * b
#
# def devide(a, b):
#     return a//b
#
# def double(a):
#     return multi(a,2)
#
# def get_something(a):
#     return  double(a) + double(a)
#
# print(multi(plus(1,2), devide(4,2)))
# print(double(5))
# print(get_something(5))

def get_something():
    return 5, 10

# _ dummy variable
x, _ = get_something()
a, b = get_something()
a    = get_something()

print({x})