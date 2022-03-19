# https://leetcode.com/problems/find-if-path-exists-in-graph/
import collections
from typing import List


# 주어진 그래프에서 시작 노드에서 목적지 노드까지 갈 수 있는지 검증하여 반환하라.
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ##############################
        ##### 실패작 ㅠㅠ 롤백이 잘안됨 ###############

        # src 노드를 기준으로 방문할 수 있는 노드들을 구한다.
        visit_list = collections.defaultdict(list)
        for edge in edges:
            visit_list[edge[0]].append(edge[1])
            visit_list[edge[1]].append(edge[0])

        # print(visit_list)  # 잘들어갔는지 확인..

        # 방문한 곳은 다시 방문하지 않는다.
        # 방문한 곳을 또 방문하면 시궁에 빠진다.
        visited = set()

        def dfs(src):
            # 방문한곳이 목적지라면 종료
            if src == destination:
                return True

            # 방문한곳을 방문한 리스트에 넣는다.
            visited.add(src)

            # 방문할 수 있는 목록을 탐색한다.
            for next_node in visit_list[src]:
                # 탐색한 곳이 방문한곳이면 무시한ㄷ.
                if next_node in visited:
                    continue
                # 탐색한곳이 아니라면 다시 dfs를 호출하여 src로 변환 후 재 탐색한다.
                if dfs(next_node):  # 결과같이 True이면 목적지니 True로 전달한다.
                    return True

            # for문이 끝날때까지 돌아갔다면, 현재 src에서는 목적지 노드가 없다는 뜻이다.
            return False

        return dfs(source)
    ##############################


sol = Solution()
print(sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
# print(sol.validPath(5, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
