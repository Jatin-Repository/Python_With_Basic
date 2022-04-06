x = {9, 2, 3, 4, 5, 6, 4}
print("Here same data-item but in integer format:{}".format(x))
print(len(x))
y = set(("9", "2", "3", "4", "5", "6", "4"))
print("Here same data-item but in string format:{}".format(y))
print(len(y))

print(type(x))

# Set generally are not ordered so direct index will not work.
print("Looping in Set")
for t in y:
    print(t)

# Adding element insert can be added since unordered hence we use add()

x.add(19)
x.add(-1)
x.add(-67)
x.add(0)
x.add(7)
y.add('65')
print(x)
print(y)

z = {5, 5, 8, 0, 78, 14}
print(z)
print(19 in z)

y.update(z)
print(y)

y.remove('3')
print(y)

y.discard(8)
print(y)

'''
y.remove(19)  # Will Prompt Error
print(y)

y.discard(19)  # No Error
print(y)

'''

print("Set y is {}".format(y))

r = y.pop()
print("Value deleted from set y is:  {}".format(r));
print(y)

s = y.pop();
print("Value deleted from set y is:  {}".format(s))
print(y)

fruits = {"apple", "banana", "cherry", "grapes", "mangoes"}

f = fruits.pop()
print(f)
print(fruits)

'''
x.clear()
print(x)

del z
print(z)  # Error z not defined
'''

t = x.union(y)
print(t)

y.update(x)
print(y)
print(x)

q = x.pop()
print(q)
print(x.pop())
print(x)

set1 = {1, 2, 3, 4, 5}
set2 = {19, 4, 12, 2, 1}
set3 = set1.intersection(set2)
print(set3)

set2.intersection_update(set1)
print(set2)

set4 = set1.symmetric_difference(set2)
print(set4)
set3.symmetric_difference_update(set2)
print(set3)

set6 = set1.difference(set2)
print(set6)

set2.difference_update(set6)
print(set2)

print(set2.isdisjoint(set1))
print(set1.issubset(set2))
print(set2.issuperset(set1))




