
class BIT:
    def __init__(self,n):
        self.data = [0]*n
        self.n = n
    def lowbit(self,x):
        return x & (-x)

    def query(self,idx):
        ans = 0
        while idx>0:
            ans += self.data[idx]
            idx -= self.lowbit(idx)
        return ans

    def rangesum(self,l,r):
        if l == 0:
            return self.query(r)
        else:
            return self.query(r) - self.query(l-1)

    def update(self,x,v=1):
        while x < self.n:
            self.data[x]+=v
            x+=self.lowbit(x)