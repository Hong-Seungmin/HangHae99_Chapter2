# https://www.acmicpc.net/problem/1874

stack = []
numList = []
result = []

n = int(input())

for i in range(n):
    numList.append(int(input()))

pushCount = 0
for n in numList:
    if not stack:
        while pushCount < n:
            pushCount += 1
            stack.append(pushCount)
            result.append('+')
        # result.append(stack.pop())
        stack.pop()
        result.append('-')
    else:
        if pushCount > n:
            if stack[-1] > n:
                print('NO')
                exit()
            for _ in range(pushCount - n):
                pop = stack.pop()
                result.append('-')
                # result.append(pop)
                if pop == n:
                    break

        else:
            for _ in range(n - pushCount):
                pushCount += 1
                stack.append(pushCount)
                result.append('+')
            # result.append(stack.pop())
            stack.pop()
            result.append('-')

for char in result:
    print(char)
# lastPopNum = 0
# for n in numList:
#     if not stack:
#         for i in range(1, n + 1):
#             stack.append(i)
#             print('+')
#     else:
#         if stack[-1] < n:
#             for i in range(stack[-1], n + 1):
#                 stack.append(i)
#                 print('+')
#         elif stack[-1] > n:
#
#     lastPopNum = stack.pop()
#     print('-')
