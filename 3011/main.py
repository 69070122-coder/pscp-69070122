"""เข็มขัดไม่สั้น"""
c1 = input()
c2 = input()
colors = {c1,c2}
if colors == {"Red", "Yellow"}:
    print("Orange")
elif colors == {"Red", "Blue"}:
    print("Violet")
elif colors == {"Yellow", "Blue"}:
    print("Green")
elif colors == {"Red"}:
    print("Red")
elif colors == {"Yellow"}:
    print("Yellow")
elif colors == {"Blue"}:
    print("Blue")
else:
    print("Error")
