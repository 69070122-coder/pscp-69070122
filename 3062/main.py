"""ticket price"""
age = int(input())
char = input().lower()

if char == "s" or 0 <= age < 18:
    print("20")
else:
    print("50")
