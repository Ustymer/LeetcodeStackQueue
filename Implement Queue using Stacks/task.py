class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
    def pop(self):
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val

    def is_empty(self):
        return self.top is None
class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)
    def pop(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()


    def peek(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()
