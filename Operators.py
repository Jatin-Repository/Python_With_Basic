
x = z = {0, 1, 2}
y = {0, 1, 2}
statement = "Memory Address for set {1}:{0}"
print(statement.format(id(x), "x"))
print(statement.format(id(y), "y"))
print(statement.format(id(z), "z"))
if x is z:
    print("Referenced objects are same")
else:
    print("Referenced objects are  not same")
if x is y:
    print("Set x and y with same value are same Address")
else:
    print("Set x and y with same value are not with same Address")

# Difference between == and is in python
# Note: id(object) give memory address for the given object

print(x == y)  # Focus on value
print(x is y)  # Focus on Memory address if same or not

print("A" in x)
print(3 not in y)


# Bitwise Operator

a = 5
b = 1
print(a | b)
print(a & b)
print(a ^ b)
print(~b)
print("1\'s Complement {}".format(~a))
print("Left Shift Operator {}" .format(a << 2))
print("Right Shift Operator {}" .format(a >> 2))


