# https://www.acmicpc.net/problem/9095

# 주어진 (1,2,3)숫자들의 합이 n이 되는 모든 경우의 수를 카운트하여 출력한다.
# 첫 줄에는 테스트케이스 숫자를 입력한다.
# 두번째줄부터 테스트케이스 만큼 n을 입력한다.
# 각 테이트케이스에 대한 출력을 각 줄에 출력한다.
###################

tc = int(input())
n = [0] * tc
for i in range(tc):
    n[i] = int(input())

nums = [1, 2, 3]

cnt = 0
for i in nums:
    result = 0
    sum = 0
    stack = [i]
    while stack:
        k = stack.pop(0)
        sum += k

        for j in nums:
            if j + sum >= n[cnt]:
                if j + sum == n[cnt]:
                    result += 1
                # sum -= k
                break
            stack.append(j)
        sum -= k

    cnt += 1
    print(result)

