from typing import *
import time

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        drr = [[a,bin(a).count('1')] for a in arr]
        drr.sort(key=lambda x:(x[1],x[0]))
        return [d[0] for d in drr]

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        lastabc = [[-1,-1,-1] for _ in range(n)]
        la = -1
        lb = -1
        lc = -1
        if s[0] == 'a':
            la = 0
        elif s[0] == 'b':
            lb = 0
        else:
            lc = 0

        for i in range(1,n):
            lastabc[i] = [la,lb,lc]

            if s[i] == 'a':
                la = i
            elif s[i] == 'b':
                lb = i
            else:
                lc = i


        cnt = 0
        for i in range(2,n):
            if s[i] == 'a':
                ii = 1
                jj = 2
            elif s[i] == 'b':
                ii = 0
                jj = 2
            else:
                ii = 0
                jj = 1
            z = min(lastabc[i][ii],lastabc[i][jj])
            if z > -1:
                cnt += z+1


        return cnt


    def countOrders(self, n: int) -> int:
        import math
        return int(math.factorial(2*n) // (2**n)) % (10**9 + 7)

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.cnt = 0
        self.discount = discount
        self.prices = {}
        for p,v in zip(products,prices):
            self.prices[p]=v

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = .0
        self.cnt += 1
        for p,a in zip(product,amount):
            total += self.prices[p] * a
        if self.cnt % self.n == 0:
            total -= self.discount * total / 100
        return total



if __name__ == '__main__':
    s = Solution()
    # print(s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
    # print(s.sortByBits([2,3,5,7,11,13,17,19]))

    # cashier = Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100])
    # print(cashier.getBill([1, 2], [1, 2]))
    # print(cashier.getBill([3, 7], [10, 10]))
    # print(cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
    # print(cashier.getBill([4], [10]))
    # print(cashier.getBill([7, 3], [10, 10]))
    # print(cashier.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))
    # print(cashier.getBill([2, 3, 5], [5, 3, 2]))

    # print(s.numberOfSubstrings('abcabc'))
    # print(s.numberOfSubstrings('aaacb'))
    # print(s.numberOfSubstrings('acb'))
    print(s.countOrders(1))
    print(s.countOrders(2))
    print(s.countOrders(3))
    print(s.countOrders(100))
    print(s.countOrders(500))

