'''frame'''
a = []

for i in range(5):
    a.append(input().strip())

longest = max(len(word) for word in a)

print('*' * (longest + 4))

for word in a:
    print('* ' + word + ' ' * (longest - len(word)) + ' *')

print('*' * (longest + 4))
