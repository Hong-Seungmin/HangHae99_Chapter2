def binary_search(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if N_array[mid] == target:
            return "yes"
        elif N_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"


N = int(input())
N_array = list(map(int, input().split()))

M = int(input())
M_array = list(map(int, input().split()))

N_array.sort()

for target in M_array:
    print(binary_search(target), end=" ")


# 5
# 8 3 7 9 2
# 3
# 5 7 9