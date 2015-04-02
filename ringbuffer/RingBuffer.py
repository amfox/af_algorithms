#coding=utf-8
__author__ = 'TIF'


class RingBuffer(object):
    class __Full(object):
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def tolist(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def __init__(self, size_max):
        self.max = size_max
        self.data = []
    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Full
    def tolist(self):
        return  self.data


if __name__ == "__main__":
    x = RingBuffer(5)
    for i in xrange(8):
        x.append(i)
        print x.__class__,x.tolist()