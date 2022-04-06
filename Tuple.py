tuple5 = ("Z", "BJP", True)
print(tuple5)
tuple6 = ("Jatin",)
tuple7 = ("Jatin")
print(tuple6)
print(type(tuple6))
print(type(tuple7))
if type(tuple6) == type(tuple7):
    print("Same type of variable")
else:
    print("Not Same type of variable")

digits = tuple(())
print(digits)

paper = tuple(("book", "copies", "paper"))
print(paper)

list7 = list(paper)

list7.append("magazine")
list7.insert(2, "booklet")

paper = tuple(list7)
print("After Conversion from tuple to list and back to tuple we have : {}".format(paper))

paper1 = tuple(paper)

paper2 = paper+paper1
print(paper2)
list10 = list(paper)
list10.remove("paper")
del list10[1]
paper = tuple(list10)
print(paper)
del list10
'''''
paper = tuple(list10)   # will give error as list10 deleted
print(paper)
'''
list11 = list(paper1)
list11.clear()
paper1 = tuple(list11)
print(paper1)


# Unpacking a Tuple

alpha = ("A", "B", "C")  # Packing a tuple
(Z, Y, X) = alpha       # unpacking a tuple
print(X)
print(Y)
print(Z)

sister = ("Jaspreet", "Harman", "Simarpreet", "Simran", "Preet", "Divya")
(*J, S, T, Q) = sister

print(J)
print(S)
print(T)
print(Q)

for s in range(len(sister)):
    print("Sister : {}".format(sister[s]))

tuple13 = tuple((1, 2, 5, 3, 5, 7, 5, 5, 6, 9, 5))
print("First Position of 5 in tuple13 is : {}".format(tuple13.index(5)))
print("Frequency of 5 in tuple13 is : {}".format(tuple13.count(5)))

listA = list(tuple13)
print(listA.index(5, 3, 7))
print(listA.count(5))





