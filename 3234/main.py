'''christmas light'''
color, n = input().split()

colors = ["Red", "Green", "Blue"]
start = "RGB".index(color)

for i in range(int(n)):
    print(colors[(start + i) % 3], end=" ")
