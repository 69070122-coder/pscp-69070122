'''check if the highest score more than lower score by more than 2'''
sum_all = float(input())
highest = float(input())

lowest = max(0,sum_all - 2*(highest))
if highest - lowest > 2:
    print("Surprising")
else:
    print("Not surprising")
