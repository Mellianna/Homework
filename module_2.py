import random
first_numder = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(first_numder)
result = []
for i in range(1, 20):
    for j in range(i+1, 20):
        if n % (i+j) == 0:
            result.append(i)
            result.append(j)

print(n)
print(*result)
