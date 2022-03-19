# https://www.acmicpc.net/problem/2606
import collections
from collections import deque
from typing import List, Tuple


# 주어진 컴퓨터와 엣지를 이용하여 바이러스의 영향권인 컴퓨터의 수를 찾아 반환한다.
# *1번 컴퓨터는 카운트에서 제외하고, 1번 컴퓨터로 인해 전파될 수 있는 컴퓨터의 수를 찾아라.
# 바이러스는 엣지에 연결된 모든 컴퓨터로 전파가 가능하고,
# 1번 컴퓨터로부터 바이러스는 시작된다.

def solution(com_num: int, edge_num: int, edges: List[Tuple[int, int]]) -> int:
    # dictionary를 이용하여 각 노드를 기준으로 연결 노드를 등록한다.
    edges_dict = collections.defaultdict(list)

    for (a, b) in edges:
        edges_dict[a].append(b)
        edges_dict[b].append(a)

    # bfs로 풀어보았다.
    def bfs(src):
        # 바이러스에 감연된 컴퓨터의 수 보관
        cnt_infected = 0

        # 감염여부를 확인한 컴퓨터 등록
        checked_list = set()

        # 감염된 컴퓨터를 탐색할 대기 목록
        queue = deque()
        # src부터 대기열 삽입
        queue.append(src)

        # 큐에 남은 컴퓨터가 없을때까지 싹다 조사한다.
        while queue:
            # 대기열의 다음 컴퓨터를 조사한다.
            node = queue.popleft()
            # 조사되지 않은 컴퓨터라면,
            if node not in checked_list:
                # 조사목록에 포함시킨다.
                checked_list.add(node)
                # 감염된 컴퓨터 수를 증가시킨다.
                cnt_infected += 1
                # 해당 컴퓨터로부터 전파될 수 있는 컴퓨터를 대기열에 넣는다.
                for next_node in edges_dict[node]:
                    queue.append(next_node)

        # 1번 컴퓨터는 카운트에서 제외한다.
        return cnt_infected - 1

    # 최초 감염지는 1번 컴퓨터이다.

    return bfs(1)


# 컴퓨터의 수를 입력한다.
c_num = int(input())
# 엣지의 수를 입력한다.
e_num = int(input())
# 각 엣지를 입력한다. => 1 2 => [(1, 2)]
edges_list = []
for _ in range(e_num):
    edges_list.append(tuple(map(int, input().split())))

print(solution(c_num, e_num, edges_list))
