# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    # dfs 방식으로 각 자리의 숫자를 +/- 이진트리로 구성 풀었다.
    def dfs(nums, sum_result):
        nonlocal answer
        # nums의 갯수가 0이면 모든 숫자들 탐색했으니 종료한다.
        if len(nums) == 0:
            # 최종 결과가 타겟과 동일하면 카운트를 올린다.
            if sum_result == target:
                answer += 1
            return

        # 이전 수식 +(더하기) 연산을 진행한다.
        dfs(nums[1:], sum_result + nums[0])
        # 이전 수식 -(빼기) 연산을 진행한다.
        dfs(nums[1:], sum_result - nums[0])

        return

    # 시작은 [모든 숫자, 0]으로 하여, sum을 0부터 계산을 시작한다.
    dfs(numbers, 0)

    return answer


# print(solution([4, 1, 2, 1], 4))
