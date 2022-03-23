# https://www.acmicpc.net/problem/1068

# 입력한 트리에서 추가 입력된 노드를 삭제한 뒤 자식노드의 갯수를 출력한다.
import collections

# 규칙에 맞게 입력값을 입력한다.
N = int(input())
nodes = list(map(int, input().split()))
target_node = int(input())

# 자식사전, 부모사전을 정의한다.
# 자식사전 : 부모를 키로 넣어 자식들을 찾는다.
# 부모사전 : 자식을 키로 넣어 부모를 찾는다.
childs = collections.defaultdict(list)
parents = collections.defaultdict(int)

# 모든 노드를 탐색하여, 부모/자식 관계를 dict에 보관한다.
for i, node in enumerate(nodes):
    if not childs[i]:
        childs[i] = []
    childs[node].append(i)
    parents[i] = node

# 지울 타겟 노드를 기준으로
# 1. 부모를 찾고,
# 2. 부모의 자식사전에서 타겟노드를 지운다.
target_parent = parents[target_node]
childs[target_parent].remove(target_node)

count = 0

# 루트부터 dfs방식으로 리프노드의 갯수를 새린다.
stack = [-1]
while stack:
    node = stack.pop()

    # 자식노드가 있다면,
    # 자식들을 스택에 넣어서 탐색을 한다.
    if childs[node]:
        for child in childs[node]:
            stack.append(child)
    # 자식이 없다면, 리프노드이므로 카운트를 증가시킨다.
    else:
        # "-1"이라면 허수 노드이므로 무시한다.
        if node != -1:
            count += 1

print(count)
