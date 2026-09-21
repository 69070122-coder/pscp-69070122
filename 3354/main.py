'''hint'''
a = input().split()
b = input().split()
c = input().split()

for i in range(1000):
    n = f"{i:03}"

    x = int(n[2])
    y = int(n[1])
    z = int(n[0])

    ok1 = (a[0] == "==" and x == int(a[1])) or \
          (a[0] == ">" and x > int(a[1])) or \
          (a[0] == "<" and x < int(a[1])) or \
          (a[0] == ">=" and x >= int(a[1])) or \
          (a[0] == "<=" and x <= int(a[1])) or \
          (a[0] == "!=" and x != int(a[1]))
    ok2 = (b[0] == "==" and y == int(b[1])) or \
          (b[0] == ">" and y > int(b[1])) or \
          (b[0] == "<" and y < int(b[1])) or \
          (b[0] == ">=" and y >= int(b[1])) or \
          (b[0] == "<=" and y <= int(b[1])) or \
          (b[0] == "!=" and y != int(b[1]))
    ok3 = (c[0] == "==" and z == int(c[1])) or \
          (c[0] == ">" and z > int(c[1])) or \
          (c[0] == "<" and z < int(c[1])) or \
          (c[0] == ">=" and z >= int(c[1])) or \
          (c[0] == "<=" and z <= int(c[1])) or \
          (c[0] == "!=" and z != int(c[1]))

    if ok1 and ok2 and ok3:
        print(n)
