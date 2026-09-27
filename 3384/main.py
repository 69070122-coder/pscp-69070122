'''pick them'''
numbers = input().strip("[]").split(",")
found = False
for number in numbers:
    number = int(number)
    if number % 2 == 0:
        print(number)
        found = True
if not found:
    print("Nope")
