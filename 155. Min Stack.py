class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ll = []
        self.topx = -1
        self.min = None
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ll.append(x)
        self.topx += 1
        if self.min == None or x < self.min:
            self.min= x
    def pop(self):
        """
        :rtype: None
        """
        if self.topx == -1:
            return None
        self.topx -= 1
        if self.ll[self.topx+1] == self.min:
            if self.topx == -1:
                self.min = None
            else:
                self.min = sorted(self.ll[0:self.topx+1])[0]
        self.ll.pop()
        return None

    def top(self):
        """
        :rtype: int
        """
        if self.topx == -1:
            return None
        return self.ll[self.topx]
    def getMin(self):
        """
        :rtype: int
        """
        if self.topx == -1:
            return None
        return self.min
'''
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]'''
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
obj.top()
obj.pop()
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.push(2147483647))
print(1,obj.top())
print(obj.getMin())
print(obj.push(-2147483648))
print(obj.top())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
