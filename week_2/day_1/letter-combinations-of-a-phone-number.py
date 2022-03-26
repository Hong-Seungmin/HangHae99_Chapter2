# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

# 주어잔 숫자열을 이용하여,
# 전화번호와 같은 문자체계에 맞게 문자열을 조합하여 반환하라.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if not digits:
            return answer
        num_to_str = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        digits_lenght = len(digits)

        # digits의 인덱스와 인덱스에 따라 작성된 sub스트링을 이용하여 재귀적으로 푼다.
        def dfs(start_index: int, sub_str: str):
            # 마지막까지 탐색했다면 결과를 등록한다.
            if start_index == digits_lenght:
                answer.append(sub_str)
                return

            ###############################
            #
            # # digits에 적혀있는 각 숫자별, 문자열의 글자 추출
            # for char in num_to_str[digits[start_index]]:
            #     # 추출된 글자를 sub스트링에 등록한다.
            #     sub_str += char
            #     # 다음 인덱스와 현재 작성된 sub스트링을 넘겨준다.
            #     dfs(start_index + 1, sub_str)
            #     # dfs에서 돌아왔다면, 현재 sub_str은 탐색이 끝났으므로,
            #     # 한칸 뒤로 가서 다시 진행한다.
            #     # "adg" => "ad" => "adh" (check) => "ad" => "adi" (check) => "ad" => "a" => "" => "b" ="bd"...
            #     sub_str = sub_str[:-1]
            # #################################

            #################################
            # digits에 적혀 있는 숫자마다 진행
            for i in range(start_index, digits_lenght):
                # 각 숫자에 대응하는 문자열의 문자마다 진행
                for char in num_to_str[digits[i]]:
                    # 다음 인덱스와 현재 sub스트링 전달
                    dfs(start_index + 1, sub_str + char)
            #################################

        dfs(0, "")
        return answer


test = Solution()
print(test.letterCombinations('23'))
