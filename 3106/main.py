'''money'''
money = int(input())
notes = [1000,500,100]
if 100 > money > 20000 or money % 100:
    print("ERROR")
else:
    for note in notes:
        count = money // note
        if count > 0:
            print(note, "=", count)
        money %= note
