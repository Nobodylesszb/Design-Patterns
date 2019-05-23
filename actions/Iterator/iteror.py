class MyIter(object):
    def __init__(self, n):
        self.index = 0
        self.n = n
    def __iter__(self):
        return self
        
    def next(self):
        if self.index < self.n:
            value = self.index**2
            self.index += 1
            return value
        else:
            raise StopIteration()

if __name__=="__main__":
    x_square=MyIter(10)
    for x in x_square:
        print (x)
