a = list()

for i in range(5):
    a.append(int(input('-->')))

max = a[0]

for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]

print(max)