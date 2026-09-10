'''cenema'''
seats = int(input())

while seats > 0:
    try:
        data = input()
    except EOFError:
        break

    if data == "":
        break

    age, tickets = map(int, data.split())

    if age < 15:
        print(-1)

    elif tickets > seats:
        print(-2)

    else:
        if age <= 22:
            price = 120
        elif age >= 60:
            price = 75
        else:
            price = 150

        total = price * tickets
        seats -= tickets

        print(total, seats)
