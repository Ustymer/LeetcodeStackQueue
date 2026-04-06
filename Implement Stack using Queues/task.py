class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val):
        node = Node(val)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def dequeue(self):
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val
    def peek(self):
        return self.head.val

    
    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x: int) -> None:
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.peek()

    
    def empty(self) -> bool:
        return self.q1.is_empty()
