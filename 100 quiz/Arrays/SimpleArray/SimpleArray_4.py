n = int(input())
a = list(map(int, input().split()))
check_true = True

for i in range(len(a)):
	if (a[i] == 0):
		print("NO")
		exit()
	else:
		check_true = True

if check_true == True:
	print("YES")
