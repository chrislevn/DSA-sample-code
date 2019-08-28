import math

n = int(input())
a = list(map(int, input().split()))
count = 0

count_div = 0

for i in range(len(a)):
    flag = 0
    if a[i] < 6 and a[i] > 0:
        if a[i] == 2 or a[i] == 3 or a[i] == 5:
            count += 1

    elif a[i] > 2:
        for x in range(2, int(math.sqrt(a[i])) + 1):
            if (a[i] % x) == 0:
                flag = 1

        if flag == 0:
            count += 1

print(count)