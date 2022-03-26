# https://leetcode.com/problems/longest-univalue-path/

# 주어진 이진트리에서 단일값으로 이루어진 가장 긴 경로의 길이를 반환한다.

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


# 중첩되는 노드간의 간선의 갯수를 세아리면 된다.
# dfs 방식으로 바닥부터 올라오면서 역으로 깊이를 세아린다.
# 자식의 값과 나의 값이 같다면, 자식이 준 length를 +1 하고,
# 값이 다르다면 length를 0으로 초기화한 뒤, 부모에게 전달(반환)한다.

# 좌우 각 자식이 같은 값을 가졌다면, 이 둘의 length를 더한 뒤 값을 비교한다.
# 부모에게는 좌우 자식 중 더 큰 length를 준 자식의 length를 전달한다.

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 가장 긴 길이를 찾아 보관한다.
        max_length = 0

        def dfs(cur_node):
            if not cur_node:
                return 0

            nonlocal max_length

            # 좌,우 노드를 추출한다.
            left_node = cur_node.left
            right_node = cur_node.right

            # 좌,우 노드의 하위 길이를 파악한다.
            left_length = dfs(left_node)
            right_length = dfs(right_node)

            # 좌,우 자식 노드의 값과 자신의 값이 일치하면 길이를 1 추가한다.(자신과 연결됨을 추가함)
            if left_node and left_node.val == cur_node.val:
                left_length += 1
            # 서로 다른값이라면 0으로 초기화하여, 자신노드부터 다시 길이를 잰다.
            else:
                left_length = 0
            if right_node and right_node.val == cur_node.val:
                right_length += 1
            else:
                right_length = 0

            # sub_length는 커브없이 쭉 이어진 길이를 준다.
            sub_length = max(left_length, right_length)
            # max_length는 커브를 포함하여 좌우모두 기록한다.
            max_length = max(max_length, left_length + right_length)

            # 부모에게는 sub_length를 주어 동일 선상의 길이를 전달한다.
            return sub_length

        dfs(root)
        return max_length
