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
    def is_empty(self):
        return self.top is None
class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        self.max_freq = max(self.max_freq, f)
        if f not in self.group:
            self.group[f] = Stack()
        self.group[f].push(val)

    def pop(self) -> int:
        res = self.group[self.max_freq].pop()
        self.freq[res] -= 1
        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1
        return res
