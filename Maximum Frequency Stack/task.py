class FreqStack:

    def __init__(self):
        self.fs1 = []
        

    def push(self, val: int) -> None:
        self.fs1.append(val)


    def pop(self) -> int:
        d = {}
        for val in self.fs1:
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        
        res = max(d, key=d.get)
        self.fs1.reverse()
        self.fs1.remove(res)
        self.fs1.reverse()
        return res
        



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
