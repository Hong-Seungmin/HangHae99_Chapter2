# https://www.acmicpc.net/problem/11725

# 입력: 첫 줄에 노드의 갯수, 둘째 줄부터 2번노드부터 N-1개의 두 노드를 적어 엣지를 입력한다.
# 출력: 첫째 줄부터 N-1개의 줄에 각 노드의 부모노드 번호를 2번 노드부터 순서대로 출력한다.
# 최상단 root는 1번이다.
import collections

N = int(input())
# 주어진 모든 노드의 짝을 보관하는 dictionary.
# 부모->자식 + 자식->부모 모두 키와 값으로 가지고 있다.
nodes = collections.defaultdict(list)

for _ in range(N-1):
    a, b = list(map(int, input().split()))
    nodes[a].append(b)
    nodes[b].append(a)

# 한번 큐에서 뽑은 노드는 큐에 넣을 필요가 없기에 visited를 생성
visited = set()

# 자식노드를 키로 하여, 본인의 부모노드를 값으로 보관한다.
childs = collections.defaultdict(int)

# 1번노드부터 탐색을 시작한다.
queue = collections.deque([1])
while queue:
    root = queue.popleft()
    # 큐에서 뽑으면 visited에 보관하여 두번 탐색을 방지한다.
    # 큐에서 노드가 나오는 순서는 부모->자식 순으로 나오게된다.
    visited.add(root)

    # 자식 노드를 큐에 보관한다.
    # visited에 들어있는 노드들은 부모(조상) 노드이므로 큐에 넣지 않는다.
    for child in nodes[root]:
        if child not in visited:
            queue.append(child)
            childs[child] = root

# dict[자식] = 부모
# dictionary를 이용하여 정렬 후 child순서에 맞게 출력한다.
for child in sorted(childs.keys()):
    print(childs[child])