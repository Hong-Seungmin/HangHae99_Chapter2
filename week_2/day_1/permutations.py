# https://leetcode.com/problems/permutations/

from typing import List


# 주어진 정수 배열을 이용하여, 모든 가능한 순열을 반환하라.
# nums = [1,2,3]
# return = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        # 재귀 속에서 작성할 수열
        sub_ans = []

        # sub_nums는 sub_ans에 포함되지 않은 수열
        def dfs(sub_nums):

            # 더이상 처리할 수열이 없으면 결과를 저장하고 리턴
            if not sub_nums:
                answer.append(sub_ans[:])
                return

            # 수열에 있는 숫자를 하나씩 꺼낸다.
            for num in sub_nums:
                # 꺼내진 숫자를 담아둔다. (수열 만드는 중 1> 12> 123> 1234 ...)
                sub_ans.append(num)
                # sub_nums는 참조변수이므로, 복사한다.
                tmp_nums = sub_nums[:]  # list[:].remove(num)하려했는데..
                # num은 sub_ans에 담았으므로 제거한다. (제거안하면 중복발생)
                tmp_nums.remove(num)  # remove는 반환이 없다.... 일일히 쳐야한다.
                dfs(tmp_nums)
                # 이전에 결과를 저장한 수열에서 마지막자리를 뺀다.
                # 마지막자리를 빼고 for문의 다음숫자를 다시 넣어야한다.
                sub_ans.pop()

        dfs(nums)
        return answer


sol = Solution()
print(sol.permute([1, 2, 3, 4]))
