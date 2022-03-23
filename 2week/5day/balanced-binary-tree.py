# https://leetcode.com/problems/balanced-binary-tree/

# 주어진 트리가 균형잡힌 이진트리인지 아닌지 확인하여 결과를 반환한다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 바텀업 방식이 무난해보이고, 탑다운방식은 아직 해법이 생각안난다.
# dfs방식으로 리프노드까지 내려간 뒤,
# 리프노드부터 부모에게 자신의 높이를 전달한다. (0부터 매번 +1씩 증가)
# 부모는 좌,우 자식에게 받은 값을 비교하고
# 2 이상이라면 음수값을 전달, (2이상이면 균형이 깨진 트리이다.)
# 0~1이라면 좌,우 중 더 큰값을 부모에게 +1 한 뒤 전달한다. (더 큰쪽이 전체 높이이므로)
# 자식에게 음수값을 전달 받은 부모는 그 값을 그대로 부모에게 전달한다.
# 최종적으로 루트노드는 음수를 전달받으면 균형이 깨진트리로 처리, (재귀일경우)
# 두 자식의 값 차이가 0~1이라면 균형잡힌 트리로 처리한다.

class Solution:
    # 루트부터 리프까지 모든 노드를 탐색하여, 균형잡힌 이진트리인지 검증한다.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []

        # (필요없다.)
        # 모든 노드들의 부모를 담고 있는 dictionary.
        # 자식노드가 부모를 찾을때 이용한다.
        parents = collections.defaultdict(TreeNode)

        # 각 노드의 높이를 저장한다.
        nodes_height = collections.defaultdict(int)

        # 스택을 거쳐간 노드들을 담고 있는 dictonary.
        # 본인 노드 차례가 왔을때 처음 호출된 것인지, 자식으로부터 올라온 것인지 확인한다.
        visited = collections.defaultdict(bool)

        # dfs방식을 위한, 노드들을 관리할 스택
        stack.append(root)

        # (필요없다.)
        # 현재 노드의 높이를 카운트 한다. 루트가 0이므로 -1부터 시작
        # height = -1

        while stack:
            node = stack.pop()

            # 노드가 값을 가지고 있다면 처리한다.
            # (리프노드의 자식(None)이 아니라면..
            if node:
                # 처음 스택에서 뽑은 노드라면(False),
                # 자식을 스택에 넣어주고 리프노드까지 진행한다.
                if not visited[node]:
                    # height += 1

                    # 다음에 뽑을때는 다른 처리를 하기 위해 값을 변경한다.
                    visited[node] = True
                    # 자식노드의 처리가 끝나면 다시 호출되게 넣어준다.
                    stack.append(node)

                    # 자식노드를 스택에 넣어준다.
                    for child in (node.left, node.right):
                        # parents[child] = node
                        stack.append(child)

                # 처음 뽑은 노드가 아니라면,(True)
                # 리프부터 올라오고 있는 중이므로,
                # 높이에 대한 연산을 처리한다.
                else:
                    # parent = parents[node]

                    # 자식노드의 높이를 추출한다.
                    left_height = nodes_height[node.left]
                    right_height = nodes_height[node.right]

                    # 높이를 비교한다.
                    # 높이의 차이가 2이상 난다면 "-1"을 주어 균형이 깨짐을 나의 높이에 기록한다.
                    # 또한, 자식의 값이 "-1"이라면 "-1"을 그대로 기록한다.
                    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                        nodes_height[node] = -1

                    # 자식트리가 균형이 잡혀있다면, 나의 노드 높이까지 더하여(+1) 나의 높이를 기록한다.
                    else:
                        nodes_height[node] = max(nodes_height[node.left], nodes_height[node.right]) + 1

                    # height -= 1

        # root의 높이 기록이 "-1"이라면 어디선가 균형이 깨진 트리이다.
        result = nodes_height[root]
        if result == -1:
            return False

        return True
