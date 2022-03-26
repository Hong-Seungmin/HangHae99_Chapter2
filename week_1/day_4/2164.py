# https://www.acmicpc.net/problem/2164

# 주제가 큐라서 큐 방식을 이용해 풀어봤다.
# 뭔가 로그함수로 풀 수 있을것 같다.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def push(self, n: int):
        newNode = Node(n)

        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        popNode = self.front
        self.front = self.front.next
        self.size -= 1

        return popNode.data

    def isEmpty(self) -> bool:
        return self.size == 0


def main():
    queue = Queue()
    lastCard = None

    n = int(input())

    for i in range(1, n + 1):
        queue.push(i)

    while not queue.isEmpty():
        lastCard = queue.pop()
        if queue.isEmpty():
            break

        lastCard = queue.pop()
        queue.push(lastCard)

    print(lastCard)


if __name__ == '__main__':
    main()
