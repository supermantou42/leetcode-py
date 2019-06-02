from typing import *


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights.copy()
        sorted_heights.sort()
        ans = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                ans += 1
        return ans

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        l = len(customers)
        max = 0
        now = 0
        base = 0
        if l <= X:
            return sum(customers)
        for i in range(l):
            if grumpy[i] == 0:
                base += customers[i]
        for i in range(X):
            if grumpy[i] == 1:
                now += customers[i]
        max = now
        for i in range(X, l):
            if grumpy[i] == 1 or grumpy[i - X] == 1:
                if grumpy[i] == 1:
                    now += customers[i]
                if grumpy[i - X] == 1:
                    now -= customers[i - X]
                if now > max:
                    max = now
        return max + base

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        m = A.copy()
        for i in range(len(m))[:0:-1]:
            m[i - 1] = min(m[i - 1], m[i])
        if m == A:
            return A
        for i in range(len(A))[::-1]:
            if A[i] != m[i]:
                for j in range(i, len(A))[::-1]:
                    if A[j] < A[i]:
                        temp = A[j]
                        A[j] = A[i]
                        A[i] = temp
                        return A
        return A

    # def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:



if __name__ == '__main__':
    s = Solution()
    # print(s.rearrangeBarcodes([2, 1, 1]))
