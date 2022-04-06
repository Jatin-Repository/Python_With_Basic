# Multi-line String
a = """My name is Jatin Deep Singh,
I am 25 year old, and I LOVE
to play cricket and badminton 
"""
print(a)

# String as Array

print(a[6])

# Loop through String

for i in "Cache Block":
    print(i)

# String length computation
print(len(a))

# Checking Phrase/Character in String

z = "Hello, Latin"
print("Hello$" in z)
if "Hello$" in z:
    print("King")
else:
    print("Long")

if "Jatin" not in z:
    print("Ukraine")
else:
    print("Germany")

# Character Checked if present or not

if "z" in "Canada":
    print("Pakistan")
else:
    print('India')

# Slicing in String


t = "Jatin , Captain Marvel "
print("Slicing:"+t[2:5])
print("Parking" [2:7])
print("Parking" [-7:2])

print("London"+t[3:1])

print("Parking" [2:3])

z = "JatinDeepSingh"
length = len(z)
print("Length of String JatinDeepSingh is: %d" % length)
print(z[:5])
print(z[-14:-1] + z[length-1:length])
print(z[-length:])

print(z[4:])

# Case

print(z.upper())

print(z.lower())

print(t.strip())

print(t.lstrip())

print(t.rstrip())

print(t.replace('J', 'L'))

print(t.replace("Jatin", "HI"))

print(t.replace("Captain", "Prime"))

# Spilt In String

a = "My,name,is,JATIN"
print(a.split(','))

# String , number combination using format()

txt = "Myself Jatin, and I am {} years old"
age = "25"
print(txt.format(age))

year = 1997
age = 25
month = 'Feb'
date = 5
name = 'Jatin'
details = "My name is {} and I was born on {}-{}-{}. I am {} year old."
print(details.format(name, date, month, year, age))
email = "jatindip500@gmail.com"
contact = 9763110542
personal = "My name is {2} amd my email id is {0} one can contact me via phone and my contact number is {1}."
print(personal.format(email, contact, name))

# Escape Character
txt = "My name is \'Jatin\' from Khalilabad"
print(txt)
