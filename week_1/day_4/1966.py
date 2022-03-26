# https://www.acmicpc.net/problem/1966

# 큐를 이용하여 풀어야한다.
# 조심해야할 부분은 우선순위가 같은데 앞서 있는 경우 가장 뒤로 밀려나야한다.
#
# 모든 우선순위에 10을 곱한 뒤 동일한 리스트를 복제하고 내림정렬한다.
# 타겟이 되는 항목에는 +1을 하여 표시한다.
# 정렬된 리스트를 기준으로 우선순위별로 pop하고,
# 목표 우선순위에 이르면 +1된 값이 나올때까지 pop한다.
def main():
    testCaseNum = int(input())
    for _ in range(testCaseNum):
        pageCnt, targetPageIndex = map(int, input().split())
        pageList = list(map(int, input().split()))

        pageList = [i * 10 for i in pageList] # [1,2,3] => [10,20,30]
        sortedPageList = sorted(pageList, reverse=True) # =>[10,20,30] => [30,20,10]
        pageList[targetPageIndex] += 1 # => [10,21,30]

        cnt = 0 # 출력 횟수
        while True:
            # 가장 먼저 뽑아야할 우선순위와 동일한 우선순위라면, or +1하여 타겟인 항목이라면, 출력처리
            # [10,10,11,10] 이라면, 10 출력, 10 출력 후 11이 출력된다.
            if pageList[0] == sortedPageList[0] or (pageList[0] - 1) == sortedPageList[0]:
                cnt += 1
                if pageList[0] % 10 == 1: # 타겟항목이라면 그만, 반복을 멈춘다.
                    break

                # 타겟 항목이 아니라면 없애버린다.
                pageList.pop(0)
                sortedPageList.pop(0)
            else:
                # 우선순위가 낮으면 뒤로 보낸다.
                pageList.append(pageList.pop(0))

        print(cnt)


if __name__ == '__main__':
    main()
