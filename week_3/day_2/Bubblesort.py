# 버블 정렬
# 인접한 두 노드를 비교하며, 정렬을 진행한다.

def bubble_sort(nums):
    length = len(nums)
    for i in range(1, length):
        for j in range(0, length - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(bubble_sort([6, 4, 8, 56]))
# => [4, 6, 8, 56]
print(bubble_sort([6, 4, 8, 56, 4, 8, 43, 1, 4, 2, 76, 9, 6, 3, 8, 9, 10, 2, 65, 8, 59]))
# => [1, 2, 2, 3, 4, 4, 4, 6, 6, 8, 8, 8, 8, 9, 9, 10, 43, 56, 59, 65, 76]
