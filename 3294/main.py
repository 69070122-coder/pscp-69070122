'''teaching time'''
n = int(input())
a = int(input())
min_time = n * a

if min_time >= 60:
    if not min_time % 60:
        print(f"{min_time // 60} hours")
    else:
        print(f"{min_time // 60} hours {min_time % 60} minute")
elif 60 > min_time > 0:
    print(f"{min_time} minute")
else:
    print("No teaching")
