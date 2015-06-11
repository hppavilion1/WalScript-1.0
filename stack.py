class StackError(Exception):
    pass

class stack(list):
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)
        
    def push(self, *items):
        for x in items:
            self.append(x)
        
    def pop(self, count = 1):
        if len(self) < count:
            raise StackError('Not enough items on stack')
        for x in range(count):
            x = self[-1]
            del self[-1]
            yield x
    
    def dup(self):
        x = self.pop()
        self.push(x, x)

    def drop(self):
        self.pop()

    def over(self):
        x = self.pop()
        y = self.pop()
        self.push(y, x, y)

    def rot(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.push(y, x, z)

    def add(self):
        x = self.pop()
        y = self.pop()
        self.push(x+y)

    def sub(self):
        x = self.pop()
        y = self.pop()
        self.push(x-y)
        
    def mult(self):
        x = self.pop()
        y = self.pop()
        self.push(x*y)
        
    def div(self):
        x = self.pop()
        y = self.pop()
        self.push(x/y)

    def mod(self):
        x = self.pop()
        y = self.pop()
        self.push(x%y)

    def negate(self):
        x = self.pop()
        self.push(-x)
