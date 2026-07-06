"""12345 67 """
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
