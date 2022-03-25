# https://leetcode.com/problems/implement-queue-using-stacks/
import copy


class Node:
    def __init__(self, x: int):
        self.data = x
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, x: int):
        if self.isFull():
            return 0

        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode
        self.count += 1

    def pop(self) -> int:
        if self.isEmpty():
            return 0

        node = self.top
        self.top = self.top.next
        self.count -= 1

        return node.data

    def getTop(self) -> int:
        if self.isEmpty():
            return 0

        return self.top.data

    def getSize(self) -> int:
        return self.count

    def isEmpty(self) -> bool:
        return self.count == 0

    def getsecond(self) -> int:
        if self.isEmpty():
            return 0
        if self.top.next:
            return 0
        node = self.top.next

        return node.data

    def isFull(self) -> bool:
        if self.getSize() >= 5:
            return True
        else : return False
        pass


# 두개의 스택으로 큐를 구현하라.
class MyQueue:

    def __init__(self):
        self.stack = Stack()
        self.stack_tmp = Stack()

    def push(self, x: int) -> None:
        if self.stack.isEmpty():
            self.stack.push(x)
        else:
            while self.stack:
                self.stack_tmp.push(self.stack.pop())
            self.stack.push(x)
            while self.stack_tmp:
                self.stack.push(self.stack_tmp.pop())

    def pop(self) -> int:
        data = self.stack.pop()

        return data

    def peek(self) -> int:
        return self.stack.getTop()

    def empty(self) -> bool:
        return self.stack.isEmpty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
