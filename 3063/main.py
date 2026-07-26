"""same problem as safe password?"""
letter = input()
digit = input()
if letter == "H" and digit == "4567":
    print("safe unlocked")
elif letter == "H" and digit != "4567":
    print("safe locked - change digit")
elif letter != "H" and digit == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
