
class UnionFind:
    def __init__(self,n):
        self.values = list(range(n))

    def union(self, p, q):
        if p == q:
            return
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return
        self.values[rp] = rq

    def find(self, x):
        if x == self.values[x]:
            return x
        x = self.find(self.values[x])
        return x

    def isconneted(self,p,q):
        if p == q:
            return True
        rp = self.find(p)
        rq = self.find(q)
        return rp == rq
