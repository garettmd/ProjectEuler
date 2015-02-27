list = []
sum = 0

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        list.append(x)

for x in list:
    sum = sum + x

print(list)

print(sum)
