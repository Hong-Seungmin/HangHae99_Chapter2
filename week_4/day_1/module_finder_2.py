def binary_search():
    start = 0
    end = N - 1
    M_index = 0

    while M_index != M:
        mid = (start + end) // 2

        if N_array[mid] == M_array[M_index]:
            flag[M_index] = True
            M_index += 1

        if N_array[mid] < M_array[M_index]:
            start = mid + 1
            end = N - 1
        elif N_array[mid] > M_array[M_index]:
            end = mid - 1

        if start >= end:
            M_index += 1


N = int(input())
N_array = list(map(int, input().split()))

M = int(input())
M_array = list(map(int, input().split()))

N_array.sort()
M_array.sort()

flag = [False for _ in range(M)]
for target in M_array:
    print(binary_search(), end=" ")

# 5
# 8 3 7 9 2
# 3
# 5 7 9
