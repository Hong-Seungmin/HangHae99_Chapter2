# https://leetcode.com/problems/diameter-of-binary-tree/

# 주어진 2진트리의 노드들을 기준으로
# 임의의 두 노드의 길이 중 가장 긴 길이를 반환한다.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 각 노드를 기준으로 좌측, 우측 각각 가장 긴 길이를 구한 뒤,
# 부모노드에게 좌우측 중 가장 긴 길이 + 자신노드(길이 1)을 더하여 전달하는 구성이다.
# 모든 자식노드는 부모노드가 있고, root노드는 자식만 있으니
# root노드부터 dfs방식으로 리프노드까지 탐색 후
# 리프노드부터 부모에게 자신의 좌우 길이를 반환하며 전달한다.
class Solution:
    def __init__(self):
        self.ans = 0

    # Optional은 None이 들어올 수 있는 변수를 지정하는 어노테이션이다.
    # 즉, root는 TreeNode 또는 None을 받을 수 있다.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 서브트리의 root를 받아, 자식노드 좌,우의 총 길이를 구하여 ans에 기록하고, (루트 기준 좌우 더하면 무조건 가장 길다.)
        # 좌,우 중 더 긴쪽을 부모에게 전달한다.
        def dfs(root):
            # None이라면, 이전 노드가 리프노드이다. 즉, 길이는 0으로 종료
            if not root:
                return 0

            # 재귀적으로 좌측과 우측 길이를 구한다.
            left, right = dfs(root.left), dfs(root.right)
            # 구한 값 중 예전의 최대길이와 비교하여 더 높은쪽을 기준으로 바꾼다.
            self.ans = max(self.ans, left + right)
            # 부모에게 좌우측 중 더 긴쪽과 부모와 자신노드의 길이 1을 더하여 전달한다.
            return max(left, right) + 1

        dfs(root)
        return self.ans
