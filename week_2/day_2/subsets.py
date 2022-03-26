# https://leetcode.com/problems/subsets/
from collections import deque
from typing import List


# 주어진 정수리스트를 이용하여, 부분집합을 모두 구하여 반환하라.
# 주어진 정수들은 중복되지 않으며, 구할 부분집합은 중복되지 않아야 한다.
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        nums_length = len(nums)

        #################################
        ## 방법 1
        #################################
        # # 기본 트리거를 만들어준다.
        # queue = deque([(0, [])])
        #
        # # [] 을 시작으로 1 > 2 > 3 ... 반복적으로 아이템에 아이템을 붙이는 과정이다.
        # while queue:
        #     # 뽑아낸 아이템을 기준으로 확장해 나간다.
        #     index, sub_nums = queue.popleft()
        #     answer.append(sub_nums)
        #     for i in range(index, nums_length):
        #         queue.append((i + 1, sub_nums + [nums[i]]))
        #
        #################################
        ## 방법 1 끝
        #################################

        # nums의 길이반복 반복하며, sub_ans에 각 항목마다 nums[i]추가를 진행한다.
        for i in range(nums_length):
            # 사이클 기준으로 sub_ans를 깊은복사하여, 새로운 반복기준을 잡아준다.
            sub_ans = answer.copy()
            # 현재 sub_ans의 모든항에 nums[i]를 추가한다.
            for node in sub_ans:
                node = node.copy()
                node.append(nums[i])

                # nums[i]를 추가한 항목을 answer에 넣어준다.
                # answer.append(node)
                answer += [node]

        return answer


sol = Solution()
print(sol.subsets([]))
print(sol.subsets([1, 2, 3]))
print(sol.subsets([1, 2, 3, 4]))
