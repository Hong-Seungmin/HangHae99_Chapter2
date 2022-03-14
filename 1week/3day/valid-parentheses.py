# https://leetcode.com/problems/valid-parentheses/

# 주어진 문자열의 괄호들이 알맞게 열리고 닫혀있는지 판단하여
# 정상적인 문자열이라면 True 아니라면 False를 반환한다.
class Solution:
    # 주어진 문자열을 스택에서 탐색한다.
    # top과 현재 문자열의 문자를 비교한다.
    # 두 문자가 같다면,
    # 스택에서 pop한 뒤, continue한다.
    # 두 문자가 다르면,
    # 현재 문자를 스택에 넣는다.
    # 문자열을 모두 탐색할때까지 반복한다.
    # 탐색 후 스택이 남아있다면, false를
    # 스택이 비었다면, true를 반환한다.
    def isValid(self, s: str) -> bool:
        # 괄호마다 비교할 괄호를 준비한다.
        compare_brackets = {'[': ']', '{': '}', '(': ')',
                            ']': '', '}': '', ')': ''}
        stack = []

        # 문자열을 차례대로 스택과 비교한다.
        for char in s:
            # 스택에 문자가 들어있고, top이 char와 같다면, 스택을 pop 한다.
            if stack and char == compare_brackets[stack[-1]]:
                stack.pop()
                continue
            # 스택에 문자가 없거나, top과 char가 다르다면, char를 스택에 push한다.
            else:
                stack.append(char)

        # 스택이 비었다면, 괄호는 정상이니 True, 스택이 남아있다면 False를 반환한다.
        return False if stack else True


print(Solution.isValid('', "{}"))
