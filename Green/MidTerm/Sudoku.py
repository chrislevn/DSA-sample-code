import collections as co

arr = []
check_row = []
small_arr = []
new_arr = []
result = True

for i in range(9):
    temp = list(map(int, input().split()))
    arr.append(temp)


transpose_arr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]


# def split_matrix(arr):
#     start
#     for i in range(3):
#         for j in range(3):
#             new_arr.append(arr[i][j])
#             a = co.Counter(new_arr)
#             for m in range(10):
#                 if a[m] > 1:
#                     return False
#
#         return True

# Matrix 9:
for i in range(6,9):
    for j in range(6, 9):
        new_arr.append(arr[i][j])
        a = co.Counter(new_arr)
        for m in range(10):
            if a[m] > 1:
                result_9 = False
                break
    result_9 = True


def check_row(row_arr):
    for i in range(len(row_arr)):
        a = co.Counter(row_arr[i])
        for j in range(10):
            if a[j] > 1:

                return False
    return True


if check_row(arr) and check_row(transpose_arr) and result == True:
    print("YES")
else:
    print("NO")