# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        dict = {}

        for i, num in enumerate(nums):
            dict[num] = (i, target - num)

        for i, num in enumerate(nums):
            key = target - num
            j, value = dict[key]
            if j != i and key + value == target:
                answer.append(i)
                answer.append(j)
                break

        return answer


sol = Solution()
print(sol.twoSum([2,5,5,11], 10))
