'''main'''
members = {}

while True:
    data = input()
    if data == "Start":
        break

    data = data.strip("{}").replace('"', '').split(":")
    name = data[0].strip()
    role = data[1].strip()
    members[name] = role

dead = {}

while True:
    name = input()
    if name == "End":
        break

    if name in members:
        dead[name] = members.pop(name)

impostor_count = 0
for role in members.values():
    if role == "Impostor":
        impostor_count += 1

print(f"{impostor_count} Impostor Remains")
print("***Alive***")

for name in sorted(members):
    print(f"{name} : {members[name]}")

print("***Dead***")

for name in sorted(dead):
    print(f"{name} : {dead[name]}")
