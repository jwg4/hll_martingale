class HyperLogLog(object):
    def __init__(self, n, k):
        self.logs = [ 0 for i in range(0, 2**n) ]

    @staticmethod
    def strength(i):
        if i % 2 == 1:
            return 0
        return 1 + strength(i / 2)

    def add_object(x):
        h = x / (2 ** n)
        r = x % (2 ** n)
        nx = strength(h)
        if nx > self.logs[r]:
            self.logs[r] = nx
