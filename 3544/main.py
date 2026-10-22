'''main'''
stock = {}

while True:
    command = input().split()
    if command[0] == "END":
        break
    elif command[0] == "ADD":
        name = command[1]
        amount = int(command[2])
        if name not in stock:
            stock[name] = 0
        stock[name] += amount
    elif command[0] == "REMOVE":
        name = command[1]
        amount = int(command[2])
        if name not in stock:
            stock[name] = 0
        if stock[name] < amount:
            stock[name] = 0
            print(f"Not enough stock for {name}")
        else:
            stock[name] -= amount
    elif command[0] == "CHECK":
        found = False
        for name in sorted(stock):
            if stock[name] < 5:
                print(name)
                found = True
        if not found:
            print("All stocks are sufficient")
    elif command[0] == "REPORT":
        for name in sorted(stock, reverse=True):
            print(f"{name}: {stock[name]}")
