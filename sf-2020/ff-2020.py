from typing import *
import time
from bisect import bisect_left
from collections import Counter
class Solution:
    def calculate(self, s: str) -> int:
        x,y = 1,0
        for ss in s:
            if ss == 'A':
                x=2*x+y
            else:
                y=2*y+x
        return x+y

    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        cs = Counter(staple)
        drinks.sort()
        ans = 0
        for k,v in cs.items():
            d = bisect_left(drinks,x-k+1)
            ans += v*d
        return ans % (10**9+7)



    def minimumOperations(self, leaves: str) -> int:
        leaves = list(leaves)
        bias = 0
        if leaves[0] == 'y':
            bias+=1
            leaves[0] = 'r'
        if leaves[-1] == 'y':
            bias+=1
            leaves[-1] = 'r'
        cov = []
        n = len(leaves)
        cnt = 1
        for i in range(1,n):
            if leaves[i] == leaves[i-1]:
                cnt+=1
            else:
                cov.append(cnt if leaves[i-1] =='y' else -cnt)
                cnt=1
        cov.append(cnt if leaves[-1] == 'y' else -cnt)
        if len(cov) == 1:
            return 1+bias
        lnow=lmin = cov[0]
        lidx=0
        for i in range(1,len(cov)):
            lnow+=cov[i]
            if lnow < lmin:
                lmin = lnow
                lidx = i
        rnow = rmin = cov[-1]
        ridx=len(cov)-1
        for i in range(len(cov)-2,-1,-1):
            rnow+=cov[i]
            if rnow < rmin:
                rmin = rnow
                ridx = i
        assert lidx <= ridx
        ans = bias
        if lidx == ridx:
            v1 = 0
            for i in range(lidx):
                if cov[i] > 0:
                    v1 += cov[i]
            v2 = 0
            for i in range(ridx+1,len(cov)):
                if cov[i] > 0:
                    v2 += cov[i]
            ans += min(v1,v2)


        else:
            for i in list(range(lidx+1))+list(range(ridx,len(cov))):
                if cov[i] > 0:
                    ans += cov[i]
            for i in range(lidx+1,ridx):
                if cov[i] < 0:
                    ans -= cov[i]
        return ans



        # leaves = list(leaves)
        # bias = 0
        # if leaves[0] == 'y':
        #     bias+=1
        #     leaves[0] = 'r'
        # if leaves[-1] == 'y':
        #     bias+=1
        #     leaves[-1] = 'r'
        # cov = []
        # n = len(leaves)
        # cnt = 1
        # for i in range(1,n):
        #     if leaves[i] == leaves[i-1]:
        #         cnt+=1
        #     else:
        #         cov.append(cnt if leaves[i-1] =='y' else -cnt)
        #         cnt=1
        # cov.append(cnt if leaves[-1] == 'y' else -cnt)
        # if len(cov) == 1:
        #     return 1+bias
        # nrl = [cov[0]]
        # nyl = [0]
        # nr, ny = cov[0],0
        # for i in range(1,len(cov)-1):
        #     if cov[i] < 0:
        #         nr-=cov[i]
        #     else:
        #         ny +=cov[i]
        #     nrl.append(nr)
        #     nyl.append(ny)
        # nr+=cov[-1]
        # nrl.append(nr)
        # nyl.append(ny)
        # n = len(cov)
        # ret = n-2
        # for i in range(1,n-1):
        #     v = nyl[i - 1] + ny - nyl[i] + nrl[i] - nrl[i - 1]
        #     ret = min(v, ret)
        #     if ret == 0:
        #         return bias
        #     for j in range(i+1,n-1):
        #         v = nyl[i - 1] + ny - nyl[j] + nrl[j] - nrl[i - 1]
        #         ret = min(v, ret)
        #         if ret == 0:
        #             return bias
        # return ret + bias

    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        r = target*2
        k = len(jump)
        dp = [0]*r
        dp[1] = inc
        def go(now,now_v):
            if dp[now] > 0:
                return dp[now]
            a = go(now-1,now_v)


        # for i in range(1,r):
        #     dp[i] = dp[i-1]+inc
        #     for j in range(k):
        #         if i % jump[j] == 0:
        #             dp[i] = min(dp[i],dp[i//jump[j]]+cost[j])
        # for i in range(r-2,0,-1):
        #     dp[i] = min(dp[i],dp[i+1]+dec)
        # return dp[target+1]


if __name__ == '__main__':
    s = Solution()
    print(s.minimumOperations("ryr"))
    print(s.minimumOperations("rrryyyrryyyrr"))
    print(s.minimumOperations("rrryyyrrrrrrrryyrr"))
    print(s.minimumOperations("rrryyyrrryyrrryyrr"))
    # print(s.busRapidTransit(target = 31, inc = 5, dec = 3, jump = [6], cost = [10]))

