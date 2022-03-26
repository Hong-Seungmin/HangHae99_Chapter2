# https://leetcode.com/problems/minimum-height-trees/
import collections
from typing import List


# 주어진 무방향 노드짝들의 리스트를 가지고,
# 가장 짧은 높이를 가진 트리의 루트노드를 반환한다.
class Solution:

    # 단순한 방법 : 각 노드를 루트로 잡고, 깊이를 측정한다. (최악일듯?)
    # 이것저것 생각하다 효율적인게 안떠올라 힌트를 봤다.
    # 리프노드를 차례차례 제거하다보면 2개 이내로 남은 노드가 최소깊이 루트 이다.
    # 기준이 없는 상황에서 맞는말이다. 한순간 같은 리프노드라면.. 가운데 기준으로 동일한 깊이라는 의미이다.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        nodes = collections.defaultdict(list)

        # 모든 노드의 연결노드를 추가한다.
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)

        node_count = n

        # 리프노드 보관
        leaves = []
        for i in range(node_count):
            if len(nodes[i]) == 1:
                leaves.append(i)

        # 마지막 2개 이하가 남을때까지 반복해서
        # 리프노드를 제거해 나간다.
        while node_count > 2:
            # 제거할 리프노드 카운트 빼기
            node_count -= len(leaves)

            # 기존 리프노드를 제거하고, 새로 생겨나는 리프노드를 추가한다.
            new_leaves = []
            for leaf in leaves:
                parent = nodes[leaf].pop()
                nodes[parent].remove(leaf)

                if len(nodes[parent]) == 1:
                    new_leaves.append(parent)

            # 새로생긴 리프노드로 바꿔준다.
            leaves = new_leaves

        # 마지막남은 리프노드를 루트로 알려준다.
        return leaves
