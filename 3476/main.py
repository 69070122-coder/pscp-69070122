'''main'''
n = int(input())

cats = {}
foxes = {}

for i in range(n):
    data = input()
    data = data.replace("{", "").replace("}", "")
    data = data.replace('"', "").replace(" ", "")
    name, kind = data.split(":")

    if kind[:3] == "Cat":
        cats[name] = kind
    else:
        foxes[name] = kind

names = {}

for name, kind in cats.items():
    names[name] = kind

for name, kind in foxes.items():
    names[name] = kind

has_cat01 = False
has_fox01 = False

for name, kind in names.items():
    if kind == "Cat01":
        has_cat01 = True
    if kind == "Fox01":
        has_fox01 = True

if not has_cat01 and "Garfield" not in names:
    cats["Garfield"] = "Cat01"

if not has_fox01 and "Fubuki" not in names:
    foxes["Fubuki"] = "Fox01"

print("Cat :", len(cats))
print("Fox :", len(foxes))

for name, kind in sorted(cats.items(), key=lambda x: int(x[1][3:])):
    print(name + ": " + kind)

for name, kind in sorted(foxes.items(), key=lambda x: int(x[1][3:])):
    print(name + ": " + kind)
