# https://leetcode.com/problems/two-sum/
import collections
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        # 딕셔너리로 처리
        dict_num = {}
        for i, num in enumerate(nums):
            key = target - num
            if key in dict_num.keys():
                answer.append(dict_num[key])
                answer.append(i)
            else:
                dict_num[num] = i

        # # 딕셔너리로 처리 실패
        # # 중복값에 대한 인덱스를 추출하기 어렵고,
        # # key = target - num 의 값이 없는 키로 나올 수 있다. (defaultdict 이용하면 무관)
        # dict = {}
        #
        # for i, num in enumerate(nums):
        #     dict[num] = (i, target - num)
        #
        # for i, num in enumerate(reversed(nums)):
        #     key = target - num
        #     j, value = dict[key]
        #     if j != i and key + value == target:
        #         answer.append(i)
        #         answer.append(j)
        #         break

        # 이것도 실패
        # # 투 포인터 방식으로 재도전 ==> 주어진 수열이 정렬된 리스트가 아니다..
        # # 아래 방식은 정렬된 방식에서 통한다.
        # i = 0
        # j = len(nums) - 1
        #
        # while True:
        #     if nums[i] + nums[j] == target:
        #         answer.append(i)
        #         answer.append(j)
        #         break
        #     if target >= 0:
        #         if nums[i] + nums[j] > target:
        #             j -= 1
        #         elif nums[i] + nums[j] < target:
        #             i += 1
        #     # 타겟이 음수라면..
        #     else:
        #         if nums[i] + nums[j] < target:
        #             j -= 1
        #         elif nums[i] + nums[j] > target:
        #             i += 1

        return answer


sol = Solution()
print(sol.twoSum([-1, -2, -3, -4, -5], -8))
