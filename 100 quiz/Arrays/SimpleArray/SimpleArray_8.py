n = int(input())
arr_a = []
arr_b = []

for i in range(n):
    a, b = map(input().split())
    arr_a.append(a)
    arr_b.append(b)

count = 0

for x in range(len(arr_a)):
    if arr_a[count] < arr_a[x] or (arr_a[count] == arr_a[x] and arr_b[count] < arr_b[x]):
        count = x

print(count+1)
