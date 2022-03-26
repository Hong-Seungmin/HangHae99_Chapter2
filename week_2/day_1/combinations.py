# https://leetcode.com/problems/combinations/
from typing import List


# 주어진 n(1~n)의 정수범위와, k(수열길이)를 이용하여
# 가능한 모든 조합을 반환하라.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 최종 답안 기록 => [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
        answer = []

        # 작성 중인 답안 임시 기록 => [1] > [1,2] > ([1,2,3]) > [1,2] > ([1,2,4]) > ...
        sub_ans = []

        def dfs(start_index):
            # 작성 중인 답의 길이가 k와 같을경우 답안에 등록한다.
            if len(sub_ans) == k:
                answer.append(sub_ans.copy())
                return

            # 시작 인덱스부터 n 까지 탐색한다.
            for i in range(start_index, n + 1):
                # 현재 탐색하는 숫자를 작성중인 답안에 넣는다.
                sub_ans.append(i)
                # i번은 작성하였으니, i+1번부터 또 작성해 나간다.
                dfs(i + 1)
                # 리턴했다는것은 작성중인 답안이 완료처리 됐다는거니 다시 뺀다.
                sub_ans.pop()

        # 1번부터 답안을 작성해 나간다.
        dfs(1)

        return answer

        ############################
        # 비교 답안, 반복구조
        # init first combination

        # nums = list(range(1, k + 1)) + [n + 1]
        #
        # output, j = [], 0
        # while j < k:
        #     # add current combination
        #     output.append(nums[:k])
        #     # increase first nums[j] by one
        #     # if nums[j] + 1 != nums[j + 1]
        #     j = 0
        #     while j < k and nums[j + 1] == nums[j] + 1:
        #         nums[j] = j + 1
        #         j += 1
        #     nums[j] += 1
        #
        # return output
        ############################


sol = Solution()
print(sol.combine(4, 3))
# print(sol.combine(1, 1))
