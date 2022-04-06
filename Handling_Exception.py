
try:
    print(x)
except Exception as e:
    print(e)
    print("Issue occurred")

p = 0
try:
    print(10/p)
except ZeroDivisionError:
    print("Second Operand can\'t be 0")
    p = int(input("Enter the second operand other than 0\n"))
finally:
    print("Division of 10 with {} is {}".format(p, 10//p))

z = (input("Enter the value for z \n"))

"""if type(z) != "<class 'int'>":
    raise Exception("Sorry, only positive value is allowed")
"""
age = int(input("Enter the voting candidate age for validation\n"))
try:
    if age > 18:
        print("Eligible for Voting!!!")
    else:
        raise ValueError
except ValueError:
    print("Sorry, not eligible for voting")

