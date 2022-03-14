# https://www.acmicpc.net/problem/9012

# 주어진 소괄호 문자열에서 괄호가 정상적으로 일치하는지 검사한다.
def isValid(s: str) -> bool:
    stack = []

    # 문자열의 소괄호를 하나씩 탐색한다.
    for char in s:
        # 스택에 비교할 소괄호가 있으면서, '(' 열림 괄호라면,
        # ')' 현재 문자가 닫힘 괄호일때 스택에서 열림 괄호를 빼낸다.
        if stack and stack[-1] == '(' and char == ')':
            stack.pop()
        # 스택이 비어있거나, 스택의 top이 닫힘괄호일때 현재 문자가 닫힘단어이거나,
        # 현재 단어가 닫힘 괄호일때 스택에 보관한다.
        else:
            stack.append(char)

        # if not stack or char == '(':
        #     stack.append(char)
        # else:
        #     stack.pop()

    # 스택이 비어있다면 괄호는 정상적이다.
    return False if stack else True


n = int(input())
brackets = []

for i in range(n):
    brackets.append(input())

for i in range(n):
    print('YES' if isValid(brackets[i]) else 'NO')
