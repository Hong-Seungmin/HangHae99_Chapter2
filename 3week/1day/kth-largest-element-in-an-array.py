# 주어진 정수 리스트에서 k 번째로 큰 숫자를 반환하라.
from typing import List


class Solution:
    # 정렬 후 k번째를 반환한다.
    # 가장 빠르게 정렬할 수 있는 힙정렬을 사용하면 된다.
    # *평균적으로 힙,병합 정렬이 속도가 무난하다.
    def findKthLargest(self, nums: List[int], k: int):
        return (sorted(nums)[len(nums)-k:])[0]


sol = Solution()
print(sol.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
