n = int(input())
arr = list(map(int, input().split()))
arr_0 = []
arr_1 = []

count_0 = 0
count_1 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        arr_1.append(count_1)
        count_0 = 0
        count_1 = 0
        count_0 += 1
    elif arr[i] == 1:
        arr_0.append(count_0)
        count_0 = 0
        count_1 = 0
        count_1 += 1


print(arr_0, arr_1)
if count_0 > 3:
    print("NO")
    exit()
elif (count_0 <= 3) and (count_1) >= 1:
    print("YES")
    exit()
