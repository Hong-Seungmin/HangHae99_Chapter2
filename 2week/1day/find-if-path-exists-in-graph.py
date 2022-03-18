# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import List


# 주어진 그래프에서 시작 노드에서 목적지 노드까지 갈 수 있는지 검증하여 반환하라.
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    #     ##############################
    #     ##### 실패작 ㅠㅠ 롤백이 잘안됨 ###############
    #     result = False
    #
    #     def dfs(src, edges):
    #         if not edges:
    #             result = False
    #         if result:
    #             return True
    #
    #         tmp_edges = edges[:]
    #
    #         for edge in edges:
    #             if destination in edge and src in edge:
    #                 return True
    #             if src in edge:
    #                 tmp_edges.remove(edge)
    #                 tmp_edge = edge[:]
    #                 tmp_edge.remove(src)
    #                 result = dfs(tmp_edge[0], tmp_edges)
    #
    #     return result
    # ##############################


sol = Solution()
# print(sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(sol.validPath(6, [[1, 3], [0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
