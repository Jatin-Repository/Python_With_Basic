j = 2
while j < 100:
    print(j)
    j *= 2

for t in range(9):
    print(t)


for t in range(0, 100, 5):
    if t > 50: print(t)  # Short Hand If

print("Hello") if 45 > 21 else print("Bye")   # Ternary Operator


# For with else
for t in range(0, 12, 2):
    print(t)
else:
    print("Loop Over")

# For with else include break and continue
for z in range(0, 30, 3):
    if z == 27: break
    print(z)
else: print("Hello")
for z in range(0, 30, 3):
    if z == 27: continue
    print(z)
else: print("Hello")
for z in range(0, 30, 3):
    if z == 33: break
    print(z)
else: print("Break not activated")

m = 1
while m < 10:
    if m == 18: continue
    print(m)
    m += 1
else: print("DON")

