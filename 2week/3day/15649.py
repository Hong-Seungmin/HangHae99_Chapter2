# https://www.acmicpc.net/problem/15649
import collections


# 주어진 N과 M을 이용하여 중복이 없는 수열을 출력하라.
# N : 수열에 나타나는 숫자
# M : 수열의 길이

# 반복문으로 시도하였다가, 재귀로 풀어버렸다.
# 부모노드 찾는게 역시나 골치였다.
# 재귀로는 그래도 손에 익어서 그런가 5분? 10분? 이내로 풀었다.

# depth는 현재 answer에 들어가 있는 문자열의 길이이다.
# M과 같을 경우 재귀를 멈춘다.
def dfs(depth):
    if depth == M:
        print(' '.join(map(str, answer)))
        return

    # 단순하게 하였다. 1~N까지 전부 탐색한다.
    # 다른방법으로는 [1~N] 리스트를 만들어서 부모노드를 지우고 반복돌리는것도 될것 같다.
    # 하지만, 메모리 먹는것보다.. 반복(아무행위도없는) 한두번 더 하는게 이득인 듯하다.
    for i in range(1, N + 1):
        # visited : 부모노드들의 흔적이다.
        # 중복이 없어야하니 부모노드와 같은 숫자는 버린다.
        if not visited[i]:
            # 결과열에 등록하고, visited에 등록하여 자식은 무시하게 만든다.
            answer.append(i)
            visited[i] = True
            # 깊이를 추가하여 다시 호출
            dfs(depth + 1)
            # 돌아왔다는것은 이 라인은 끝났다는것이니 pop 해준다.
            answer.pop()
            visited[i] = False


N, M = map(int, input().split())
visited = collections.defaultdict(bool)
answer = []

dfs(0)
