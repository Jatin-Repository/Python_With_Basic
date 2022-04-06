"""
List allow duplicate and has specified order, represented by square bracket[] .
Order can be changed with help of inbuilt functions.
"""

name = ['Jatin', 'Deep', 'Taran', 'Deep']

print(len(name))
print(name[0])
print(id(name[1]))
print(id(name[3]))
print("Break\n")
print(id(id(name[1])))
print(id(id(name[3])))
print("Break\n")
print(name[1] == name[3])
print(name[1] is name[3])
print("Break\n")
print(id(id(name[1])) is id(id(name[3])))


list4 = ["Jatin", 25, 'skin', 42.3, True, {"King", 1767}]
print(list4)

# list constructor for creating new list
party = list(('BJP', 'BSP', 'INC'))
print(party)

# Accessing List item
print(list4[1])
print(list4[-1])

Alpha = ['A', 'B', 'C', 'D']
Alpha[2:4] = ['M', 'N', 'G', 'H']
print(Alpha)
a = ['A', 'B', 'C', 'D']
a[1:6] = ['E']
print(a)
print(len(a))


# insert in a list
b = ['A', 'B', 'C']

b.insert(1, 'D')
print(b)

b.insert(-1, 'D')
print(b)

b.insert(-9, 'D')
print(b)

b.append('Z')
print(b)

character = c = ["A", "B", "C", "D"]
digits = [0, 1, 2, 3]
character.extend(digits)
print(character)
d = {11, 12, 13, 14}
c.extend(d)
print(c)

d.remove(13)
print(d)

character.remove('B')
print(character)

digits.pop(1)
print(digits)

del c
# print(c) // Error since physical structure is removed.

del character[2]
print(character)

digits.clear()
print(digits)

tea = ['11', '12', '33', '14', '25', '10']
temp = []
for x in tea:
    if '1' in x:
        temp.append(x)
print(temp)

# List Comprehension (Short-cut of above)
tally = []
tally = [x for x in tea if "1" in x]
print("ShotCut:{}".format(tally))

beta = ["F", "e", "a", "B"]
alpha = list(beta)
beta.sort()
print(beta)
beta.sort(reverse=True)
print(beta)
print("Alone:{}".format(alpha))
alpha.sort(key=str.lower)
print("Hello:{}".format(alpha))

thislist = ["banana", "Orange", "kiwi", "Apple"]
thislist.sort(key=str.lower)
print(thislist)

thislist.reverse()
print(thislist)


# Join two list

list3 = alpha+thislist+beta
print(list3)

list4 = beta.extend(alpha)
for t in beta:
    alpha.append(t)
print(alpha)
print(list4)

(p, q, r) = (15, 20, 9)
print(p, q, r)

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement")

for x in range(0.5, 5.5, 0.5):
  print(x)
