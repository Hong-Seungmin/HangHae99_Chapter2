# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# 주어진 문자열을 이용하여, 트리를 만들고,
# 트리를 다시 문자열로 만드는 직렬화/역직렬화 함수를 만든다.

# 코드자체가 난해한것 없이, 코드 그 자체를 받아들이면되기에
# 별도 설명은 적지않았다.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # 트리의 root를 받아서 트리의 요소를 문자열로 반환한다.
    # bfs방식으로 노드를 하나씩 리스트에 넣고, 리스트를 문자열로 전환하였다.
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        answer = []

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                answer.append("null")
            else:
                answer.append(str(node.val))
                for child in (node.left, node.right):
                    queue.append(child)

        return ','.join(answer)

    # 주어진 문자열을 트리로 구성한 뒤, 루트노트를 반환한다.
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) <= 0:
            return None

        data_list = data.split(',')
        index = 0

        root = TreeNode(data_list[index])
        queue = deque([root])
        while queue:
            node = queue.popleft()

            index += 1
            if data_list[index] != "null":
                node.left = TreeNode(int(data_list[index]))
                queue.append(node.left)
            index += 1
            if data_list[index] != "null":
                node.right = TreeNode(int(data_list[index]))
                queue.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
