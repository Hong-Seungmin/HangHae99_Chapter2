# https://leetcode.com/problems/implement-stack-using-queues/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def push(self, x: int):
        newNode = Node(x)

        if self.count == 0:
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.count += 1

    def peek(self) -> Node:
        return self.front

    def pop(self) -> Node:
        node = self.front
        self.front = node.next
        self.count -= 1

        return node

    def getSize(self) -> int:
        return self.count

    def isEmpty(self) -> bool:
        return self.count == 0


# 큐를 이용하여 스택을 구현해 보자.
class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        for _ in range(self.queue.getSize() - 1):
            node = self.queue.pop()
            self.queue.push(node.data)
        node = self.queue.pop()

        return node.data

    def top(self) -> int:
        for _ in range(self.queue.getSize() - 1):
            node = self.queue.pop()
            self.queue.push(node.data)
        node = self.queue.peek()
        self.queue.pop()
        self.queue.push(node.data)

        return node.data

    def empty(self) -> bool:
        return self.queue.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
