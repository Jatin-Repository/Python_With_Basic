detail = {
    "name": "jatin",
    "age": 25,
    "dob": "05-02-1997",
    "contact": 9717110842,
    "dob": "05-feb-1997"
}
print(detail)
print(detail["dob"])  # Update by last DOB
print("Fetching using get function: %s" % (detail.get("dob")))
print(len(detail))  # No duplicate is allowed
print(type(detail))
print(detail.keys())
print(detail.values())
p = detail.items()
print(p)

if "dob" in detail:
    print(detail.get("name"))

# Update the entries
detail.update({"name": "Jatin Deep"})
print(detail)

detail.update({"email": "Jatin@gmail.com"})  # email not exist it automatically added
print(detail)

detail["College"] = "Galgotia College"
print(detail)

information = detail.copy()

detail.pop("age")
print(detail)

detail.popitem()   # last added key is removed from dictionary detail
print(detail)

del detail["contact"]
print(detail)

detail.clear()
print(detail)

"""
del detail
print(detail)    # Error for detail is not defined

"""
print("Keys")
for t in information.keys():
    print(t)
print("Values")
for z in information.values():
    print(z)
for r, s in information.items():
    print("Key: {} \t Value:{}".format(r, s))

info = dict(information)
print(info)

# Nested Dictionary

myHome = {
    "Papa": {
        "name": "Bhupendra Pal Singh",
        "age": 50
    },
    "Mom": {
        "name": "Gurmit Kaur",
        "age": 43
    }
}
print(myHome)

Father = {
        "name": "Bhupendra Pal Singh",
        "age": 50
}
Mother = {
        "name": "Gurmit Kaur",
        "age": 43
}

Family = {
    "Daddy": Father,
    "Mommy": Mother
}

print(Family)

# default assigning in dictionary

X = ['a', 'b', 'c']
Y = 14
Z = dict.fromkeys(X, Y)
print(Z)

T = dict.fromkeys(X)
print(T)
P = dict(Z)
z = T.setdefault('b')
y = T.setdefault('b', "18")
if z == y and z is not None:
    print(z)
else:
    print("OOH!.....")
p = T.setdefault("r")
q = P.setdefault("r", 19)
if p == q:
    print(q)
else:
    print("Not Equal")
    print("r value added to dictionary T: %s" % p)
    print("r value added to dictionary P: %s" % q)
print(T)
print(P)
