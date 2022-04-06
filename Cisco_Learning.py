# None Values
x = None
y = 5
print(x)
"""if y > x:
    print(x)
else:
    print(x)"""

"""z = None + y * 10
print(z)"""


def fun():
    return


print(fun())


def fun(t):
    t += 1
    return t


x = 2
x = fun(x * 10)
print(x)

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
print("First:"+v)
for k in range(len(dictionary)):
    print(k)
    v = dictionary[v]
    print("Middle:"+v)
print(v)

# tuple don't support assignment
"""my_tuple = tuple([5, 4])

my_tuple[1] = my_tuple[1]+my_tuple[0]

print(my_tuple)"""


def function(p=0):
    return p


print(function())
print(function("Str"))
tup = (1, 2, 4, 8)
tup = tup[1:-1]
print("Firstly:{}".format(tup))
tup = tup[0]
print(tup)

n = 0
m = 10
o = n < m and n > m or m > n and n < m
print(o)

try:
    print(5//'0')
except (ValueError, ZeroDivisionError):
    print("Too Bad")
except:
    print("Hello")

try:
    value = input("Enter the number\n")
    print(int(value)/len(value))
except ValueError:
    print("Check the value")
except ZeroDivisionError:
    print("Length of input is 0")
except TypeError:
    print("Check DataType")
except Exception as e:
    print(e)
    print("Bye")

mylist = [x*x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(mylist))


print("a", "b", "c", sep="sep")
print("a", "b", "c", end="....\n")
print("a", "b", "c", sep="$", end="~\n")


"""def add(a=9, b=6):
    return a ** b

print(add(b=6, 4))"""

"""foo = (1, 2, 3)
print(foo.index("0"))"""

print = 45
print(print)

