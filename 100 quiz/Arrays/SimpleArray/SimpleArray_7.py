n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

for i in range(len(arr) - 1):

    remain = arr[i + 1] - arr[i]
    if remain > 1:
        print(arr[i] + 1)
        exit()
if arr[len(arr) - 1] - arr[len(arr) - 2] == 1:
    print(arr[len(arr) - 1] + 1)