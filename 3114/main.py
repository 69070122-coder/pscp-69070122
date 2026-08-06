'''suvannaphum parking spot'''
h1, m1 = map(int, input().split("."))
h2, m2 = map(int, input().split("."))

t = (h2 * 60 + m2) - (h1 * 60 + m1)

if t < 0 or t > 1440:
    print("ERROR")
elif t <= 15:
    print("FREE")
else:
    h = (t + 59) // 60 # ปัดเศษชั่วโมง
    if h == 1:
        print(25)
    elif h == 2:
        print(50)
    elif h == 3:
        print(80)
    elif h == 4:
        print(110)
    elif h == 5:
        print(145)
    elif h == 6:
        print(180)
    else:
        print(250)
