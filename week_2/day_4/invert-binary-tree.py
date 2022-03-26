# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


# 주어진 이진트리를 좌우반전시켜 반환한다.
#     1       ==>       1
#   2   3     ==>     3   2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 생각보다 어렵지 않은 문제이다.
# 반전의 특성을 따져보면, 부모기준에서 자식노드를 바꿔주면
# 결국엔 전체가 다 바뀌게된다.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs, dfs 모두 될것으로 예상되지만,
        # bfs를 몇번 안써봐서 큐를 활용하였다.
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                # 자식을 큐 대기열에 넣어 다음 순번으로 넘겨준다.
                queue.append(node.left)
                queue.append(node.right)
                # 자식노드의 위치를 바꿔준다.
                node.left, node.right = node.right, node.left

        return root
