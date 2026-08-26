'''conan'''
text = input()
k = int(input())

result = ""

for char in text:
    result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))

print(result)
