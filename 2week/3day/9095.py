# https://www.acmicpc.net/problem/9095

# 주어진 (1,2,3)숫자들의 합이 n이 되는 모든 경우의 수를 카운트하여 출력한다.
# 첫 줄에는 테스트케이스 숫자를 입력한다.
# 두번째줄부터 테스트케이스 만큼 n을 입력한다.
# 각 테이트케이스에 대한 출력을 각 줄에 출력한다.
###################

# dfs방식으로 재귀적으로 풀었다.
# dfs에서 n과 sum을 받아 매번 비교하고,
# 통과되지 않으면, sum을 + i(1,2,3) 하며 dfs호출한다.
# sum은 1씩 증가하므로 n 보다 큰수는 나오지 않게하기 위해
# 통과된다면 다음 수로 넘어가지않게끔 break하였다.
def dfs(n, sum):
    # cnt를 전역변수에서 불러온다.
    global cnt

    # sum이 n이상이 될경우 (실질적으로는 sum은 n 까지만 동작한다.)
    # cnt를 증가시키고 false를 반환하여 다음 이웃노드로 못가게 한다.
    if sum >= n:
        cnt += 1
        return False

    # 현재 노드의 자식(nums)들을 순차적으로 호출한다.
    for i in nums:
        # dfs가 false이면 해당 자식노드에서 결과가 나왔으니 다음 자식노드는 볼 필요없다.
        if not dfs(n, sum+i):
            break
    # - 모든 자식노드를 탐색하여도 결과(sum==n)가 없다면 True를 반환하여 이웃을 탐색한다.
    # - 더이상 이웃이 없다면 현재 자식노드들에서는 결과가 없다는거니 부모노드를 다음으로 바꾸게 된다.
    return True


# tc : 테스트케이스 수량 입력
# n[] : 각 순서에 맞게 n 입력
tc = int(input())
n = [0] * tc
for i in range(tc):
    n[i] = int(input())

# nums 정의
nums = [1, 2, 3]

# 테스트케이스별 결과 처리
for i in range(tc):
    cnt = 0
    dfs(n[i], 0)
    print(cnt)


# # 반복문으로 어찌저찌 하려 했는데 잘되지 않았다...
# # 역시 매번 겪는.. 이전 노드에 대한 값 처리가 안되었다..
# # *잘안된 이유 : 실패 or 성공할경우 이웃노드로 전환하기 전에 sum에서 현재 노드값을 빼줘야한다.
#
# cnt = 0
# for i in nums:
#     result = 0
#     sum = 0
#     stack = [i]
#     while stack:
#         k = stack.pop(0)
#         sum += k
#
#         for j in nums:
#             if j + sum >= n[cnt]:
#                 if j + sum == n[cnt]:
#                     result += 1
#                 # sum -= k
#                 break
#             stack.append(j)
#         sum -= k
#
#     cnt += 1
#     print(result)
#

