# https://www.acmicpc.net/problem/1966

# 큐를 이용하여 풀어야한다.
# 조심해야할 부분은 우선순위가 낮은데 앞서 있는 경우 가장 뒤로 밀려나야한다.
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

        pageList = [i * 10 for i in pageList]
        sortedPageList = sorted(pageList, reverse=True)
        pageList[targetPageIndex] += 1

        cnt = 0
        while True:
            if pageList[0] == sortedPageList[0] or (pageList[0] - 1) == sortedPageList[0]:
                cnt += 1
                if pageList[0] % 10 == 1:
                    break
                pageList.pop(0)
                sortedPageList.pop(0)
            else:
                pageList.append(pageList.pop(0))

        print(cnt)


if __name__ == '__main__':
    main()
