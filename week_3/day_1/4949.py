# https://www.acmicpc.net/problem/4949
# 심심풀이 문제풀기

# 주어진 문자열에서 괄호가 제대로 들어가있는지 확인한다.
# 정상이라면 "Yes", 아니라면 "No"를 각 줄마다 출력한다.
# 입력된 문자열이 "." 이라면 종료한다.

brackets = {'(': ')', '[': ']'}

while True:
    stack = []
    check = True
    _str = input()
    if _str == ".":
        break

    for char in _str:
        if char in brackets.keys():
            stack.append(char)

        elif char in brackets.values():
            if stack:
                if char == brackets[stack.pop()]:
                    continue

            check = False
            break

    if check and not stack:
        print("Yes")
    else:
        print("No")
