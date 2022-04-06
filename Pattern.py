"""def display_Array(t):
    for m in range(len(t)):
        for n in range(len(t[m])):
            print(t[m][n], end=' ')
        print()


row = int(input("Enter the number of row for array\n"))
col = int(input("Enter the number of column for array\n"))
Array = list(list())
print("Enter the values in array\n")
for i in range(0, row):
    temp = list()
    for j in range(0, col):
        x = int(input())
        temp.insert(j, x)
    Array.insert(i, temp)
print(Array[2])
print(len(Array))
print(len(Array[0]))
display_Array(Array)

array1 = list(list())"""

"""
# Triangle
def triangle(r):
    mid = r
    print(mid)
    for L in range(0, r):
        for K in range(0, (2*r)):
            if K in range(mid-L, mid+L+1):
                count = "1"
            else:
                count = " "
            print(count+" ", end=" ")
        print()

print(triangle(5))
"""


def pascal_triangle(p):
    middle = p
    #  print(middle)
    list3 = list(list())
    for P in range(0, p):
        list4 = list()
        if P == 0:
            list4 = list([1, ])
            list3.insert(P, list4)
            P += 1
            continue
        else:
            for Q in range(0, P):
                if Q in range(1, P-1):
                    list5 = list(list3[P-1])
                    x = list5[Q-1]+list5[Q]
                else:
                    x = 1
                list4.insert(Q, x)
        list3.insert(P, list4)
    del list3[0]
    return list3


print(pascal_triangle(6))

y = pascal_triangle(5)
list6 = list()
length5 = len(y)
for A in range(0, length5):
    list7 = y[A]
    length6 = len(list7)
    for B in range(0, length6):
        z = list7[B]
        list6.append(z)
print(list6)
