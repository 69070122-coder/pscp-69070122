'''mini game'''
G = int(input())
Y = int(input())
if G not in range(1, 7) or Y not in range(1, 7):
    print("Invalid")
elif G == Y:
    print("Correct!")
else:
    print("Wrong!")
