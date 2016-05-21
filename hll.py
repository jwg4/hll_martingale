import logging


class HyperLogLog(object):
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.logs = [ 0 for i in range(0, 2**n) ]

    def strength(self, i):
        if i == 0:
            return self.k
        if i % 2 == 1:
            return 0
        return 1 + self.strength(i / 2)

    def add_object(self, x):
        h = x // (2 ** self.n)
        r = x % (2 ** self.n)
        nx = self.strength(h)
        if nx > self.logs[r]:
            self.logs[r] = nx
            return True
        return False

    def add_objects(self, l):
        for x in l:
            self.add_object(x)

    @property
    def unadjusted_count(self):
        sum = 0
        for x in self.logs:
            sum = sum + 2**(0-x)
        return 2**(self.k) / sum

class MartingaleHyperLogLog(HyperLogLog):
    count = 0

    def add_object(self, x):
        count = self.get_count()
        if super(MartingaleHyperLogLog, self).add_object(x):
            self.count = self.count + count
    
    def get_count(self):
        p = 0
        for i in self.logs:
            p = p + 2**(0-i)
        p = p / (2**self.n)
        logging.debug("%f, %f" % (p, 1/p))
        return 1 / p

