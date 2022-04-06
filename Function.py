def multiply(a, b=7):
    print(a*b)


def add(a=12, b=6):
    print(a+b)


multiply(3, 5)
multiply(7)
add(3, 5)
# add( , 7)   Syntax Error
add(7, )
add()


def fruits(apple):
    for t in apple:
        print(t)


units = ["mango", "apple", "peach"]
fruits(units)


def add(x, y):
    print("Multiplication of x: {} and y: {} = {}".format(x, y, x*y))


print(add(2, 3))
print(type(add(7, 9)))


def factorial(m):
    if m == 0 or m == 1:
        result = 1
    else:
        result = m * factorial(m-1)
    return result


t = int(input("Enter the number\n"))
print("Factorial of the given number {} is {}".format(t, factorial(t)))



