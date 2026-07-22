'''module for fining the overlap of 
rectangle and area of the overlap'''
x1 , y1, lenght1, height1 = list(map(int,input().split()))
x2 , y2, lenght2, height2 = list(map(int,input().split()))
left = max(x1,x2)
right = min ( x1+lenght1 , x2+lenght2 )
top = min( y1+height1 , y2+height2 )
bottom = max(y1, y2)
if right <= left or top <= bottom:
    print("no overlapping")
else:
    print(f"{(right-left)*(top-bottom)}")
