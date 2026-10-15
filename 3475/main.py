'''main'''
menu = []

while True:
    text = input()
    if text == "DONE":
        break
    if text == "CLOSED":
        menu = []
        break
    if text == "SOMETHING'S WRONG":
        menu = []
    elif text.startswith("Can't do: "):
        food = text[10:]
        if food in menu:
            menu.remove(food)
    else:
        food, course = text.rsplit(" #", 1)
        if course == "N":
            menu.append(food)
        else:
            menu.insert(int(course) - 1, food)

print(f"Full Course: {menu} Reversed: {menu[::-1]}")
