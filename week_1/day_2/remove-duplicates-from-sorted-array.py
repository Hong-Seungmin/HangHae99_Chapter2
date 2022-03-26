from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        
        for i in range(len(nums)):
            if i + cnt == len(nums):
                break

            if nums[i] == nums[i + 1]:
                cnt += 1
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]

        return cnt
