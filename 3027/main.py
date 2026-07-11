"""67"""
x,y,z = list(map(int,input().split()))
price = int(input())
total = ((x + y)*2)*z
totalPrice = total*price
print(total)
print(totalPrice)
