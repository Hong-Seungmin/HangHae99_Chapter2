# https://leetcode.com/problems/diameter-of-binary-tree/

# 주어진 2진트리의 노드들을 기준으로
# 임의의 두 노드의 길이 중 가장 긴 길이를 반환한다.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # 각 노드를 기준으로 좌측, 우측 각각 가장 긴 길이를 구한 뒤,
# # 부모노드에게 좌우측 중 가장 긴 길이 + 자신노드(길이 1)을 더하여 전달하는 구성이다.
# # 모든 자식노드는 부모노드가 있고, root노드는 자식만 있으니
# # root노드부터 dfs방식으로 리프노드까지 탐색 후
# # 리프노드부터 부모에게 자신의 좌우 길이를 반환하며 전달한다.
# class Solution:
#     def __init__(self):
#         self.ans = 0
#
#     # Optional은 None이 들어올 수 있는 변수를 지정하는 어노테이션이다.
#     # 즉, root는 TreeNode 또는 None을 받을 수 있다.
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # 서브트리의 root를 받아, 자식노드 좌,우의 총 길이를 구하여 ans에 기록하고, (루트 기준 좌우 더하면 무조건 가장 길다.)
#         # 좌,우 중 더 긴쪽을 부모에게 전달한다.
#         def dfs(root):
#             # None이라면, 이전 노드가 리프노드이다. 즉, 길이는 0으로 종료
#             if not root:
#                 return 0
#
#             # 재귀적으로 좌측과 우측 길이를 구한다.
#             left, right = dfs(root.left), dfs(root.right)
#             # 구한 값 중 예전의 최대길이와 비교하여 더 높은쪽을 기준으로 바꾼다.
#             self.ans = max(self.ans, left + right)
#             # 부모에게 좌우측 중 더 긴쪽과 부모와 자신노드의 길이 1을 더하여 전달한다.
#             return max(left, right) + 1
#
#         dfs(root)
#         return self.ans


############################
#### dfs를 반복문으로 푸는것을 찾았다.
from enum import Enum


# 노드의 상태를 표시한다.
# self : 처음 나타난 노드
# children : 스택에 들어갔다 나온 경험 있는 노드
# children은 아마 부모노드의 데이터를 기록하기 위한 장치같다.. 내가 찾던 구현법이다.
class State(Enum):
    SELF = 0
    CHILDREN = 1


# 노드의 정보를 담는 객체
class NodeState:
    def __init__(self, node: TreeNode, state: State = State.SELF):
        self.node = node
        self.state = state


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        if root is None:
            return diameter

        # 각 노드들의 하위의 길이를 보관하는 dict이다. -1로 초기화
        heights: Dict[TreeNode, int] = {None: -1}

        # 루트노드부터 dfs 탐색을 시작한다.
        stack = [NodeState(root)]
        while stack:
            cur = stack.pop()

            # 처음 나타난 노드라면,
            if cur.state == State.SELF:  # 1st encounter, push the children
                # children처리한 뒤, 자식노드를 모두 처리하고,
                # 다시 현재 노드가 스택에서 나온다면, 연산을하게 된다.
                cur.state = State.CHILDREN

                # 스택에 다시 넣어 dfs방식의 순서에 맞게 처리한다.
                # 현재 노드를 지금 스택에 넣고, 이후 자식노드들 스택에 쌓으면 dfs 방식이 구현된다.
                stack.append(cur)

                # 현재 노드의 모든 자식을 스택에 넣는다.
                for child_node in (cur.node.left, cur.node.right):
                    if child_node is not None:
                        stack.append(NodeState(child_node))
            # 처음이 아니라면,
            else:  # 2nd encounter, process it
                # 자식노드의 길이를 구한다. 리프노드라면 -1일 것이다.
                # *-1인 이유는... 나중에 자신의 길이를 +1 하기에 0을 맞추기 위함인 듯 하다.
                left_height = heights[cur.node.left]
                right_height = heights[cur.node.right]

                # 자식노드 중 더 큰 노드의 길이에 자신의 길이 1을 더하고, 자신의 길이를 보관한다.
                heights[cur.node] = max(left_height, right_height) + 1
                # 지름값을 갱신한다.
                diameter = max(diameter, left_height + right_height + 2)

        return diameter

############################
