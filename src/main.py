n = 5

for i in range(0, n):
    if i == 3:
        continue
    print(i ** 2)

print("================")

i = 0
while i < n:
    if i == 3:
        i += 1
        continue
    print(i ** 2)
    i += 1