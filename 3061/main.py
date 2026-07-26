'''pass or not'''
midterm = int(input())
final = int(input())
over_all = midterm + final
print(over_all)
if over_all >= 50:
    print("pass")
else:
    print("fail")
