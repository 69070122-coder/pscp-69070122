'''shipment company'''
first,second = input().split()
weight = float(input())

if first == "BKK" and second == "CNX":
    print(f"{10 + 30*(weight):.2f}")
elif first == "BKK" and second == "PKT":
    print(f"{25 + 50 *(weight):.2f}")
elif first == "CNX" and second == "UBP":
    print(f"{15 + 40*(weight):.2f}")
elif first == "UBP" and second == "BKK":
    print(f"{20 + 40*(weight):.2f}")
elif first == "UBP" and second == "PKT":
    print(f"{40 + 70*(weight):.2f}")
elif first == "PKT" and second == "CNX":
    print(f"{30+60*(weight):.2f}")
else:
    print("Error")
