n = int(input())
h = list(map(int, input().split()))
sum_arr = []

min_num = min(h)


for i in range(len(h)):
    remain = 0
    remain = h[i] - min_num
    sum_arr.append(remain)

print(sum(sum_arr))