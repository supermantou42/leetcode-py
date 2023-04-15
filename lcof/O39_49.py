from typing import *
import collections
import heapq

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = -1
        v = 0
        n = len(nums)
        for i in range(n):
            if v == 0:
                t = nums[i]
                v = 1
            else:
                if nums[i] == t:
                    v+=1
                else:
                    v-=1
        return t

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        miniheap = [-a for a in arr[:k]]
        heapq.heapify(miniheap)
        for i in range(k,n):
            if arr[i] < -miniheap[0]:
                heapq.heappushpop(miniheap,-arr[i])
        return [-a for a in miniheap]

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        d = [0] * n
        d[0] = 0 if nums[0] < 0 else nums[0]
        for i in range(1,n):
            d[i] = max(d[i-1],0) + nums[i]
        return max(d)

    def countDigitOne(self, n: int) -> int:
        b = 1
        ans = 0
        p = 0
        q = n
        while True:
            d = q % 10
            q //= 10
            if d == 0:
                ans += q * b
            elif d == 1:
                ans += q * b + p + 1
            else:
                ans += (q+1)*b

            p += d * b
            b *= 10
            if q == 0:
                return ans

    def findNthDigit(self, n: int) -> int:
        if n == 0:
            return 0
        t = 9
        b = 1
        k = 1
        while n > t:
            n = n - t
            b *= 10
            k += 1
            t = 9 * b * k
        return int(str(b+(n-1)//k)[(n-1)%k])


    def minNumber(self, nums: List[int]) -> str:
        import functools
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        dp = [1]*n
        for i in range(1,n):
            dp[i] = dp[i-1]
            if num[i-1] == '1' or (num[i-1] == '2' and '0' <= num[i] <= '5'):
                dp[i] += dp[i-2]
        return dp[-1]

    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

    def lengthOfLongestSubstring(self, s: str) -> int:
        s = [ord(ss) for ss in s]
        lastshowidx = [-1]*256
        n = len(s)
        table = [-1]*n
        for i in range(n):
            table[i] = lastshowidx[s[i]]
            lastshowidx[s[i]] = i
        ans = 1
        cur = 1
        for i in range(1,n):
            if table[i] < i - cur:
                cur+=1
                ans = max(ans,cur)
            else:
                cur= i - table[i]
        return ans

    def nthUglyNumber(self, n: int) -> int:
        i,j,k = 0,0,0
        dp = [0]*n
        dp[0] = 1
        for t in range(1,n):
            ii = 2*dp[i]
            jj = 3*dp[j]
            kk = 5*dp[k]
            dp[t] = min(ii,jj,kk)
            if dp[t] == ii:
                i+=1
            if dp[t] == jj:
                j+=1
            if dp[t] == kk:
                k+=1
        return dp[-1]

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = [] # max-heap
        self.heap2 = [] # min-heap

    def addNum(self, num: int) -> None:
        if len(self.heap1) == len(self.heap2):
            heapq.heappush(self.heap1, -heapq.heappushpop(self.heap2, num))
        else:
            heapq.heappush(self.heap2, -heapq.heappushpop(self.heap1, -num))

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            if len(self.heap1) == 0:
                return 0
            return (-self.heap1[0]+self.heap2[0])/2
        else:
            return -self.heap1[0]





if __name__ == '__main__':
    s = Solution()
    # print(s.getLeastNumbers(arr = [0,1,2,1], k = 1))
    # print(s.findNthDigit(666))
    # m = MedianFinder()
    # case = [[40], [], [12], [], [16], [], [14], [], [35], [], [19], [], [34], [], [35], [], [28], [], [35], [], [26], [],
    #  [6], [], [8], [], [2], [], [14], [], [25], [], [25], [], [4], [], [33], [], [18], [], [10], [], [14], [], [27], [],
    #  [3], [], [35], [], [13], [], [24], [], [27], [], [14], [], [5], [], [0], [], [38], [], [19], [], [25], [], [11],
    #  [], [14], [], [31], [], [30], [], [11], [], [31], [], [0], []]
    #
    # for c in case:
    #     if c:
    #         m.addNum(c[0])
    #     else:
    #         print(m.findMedian())

    # m.addNum(-1)
    # print(m.findMedian())
    # m.addNum(-2)
    # print(m.findMedian())
    # m.addNum(-3)
    # print(m.findMedian())
    # m.addNum(-4)
    # print(m.findMedian())
    # m.addNum(-5)
    # print(m.findMedian())

    # print(s.lengthOfLongestSubstring('abcabcbb'))
    # print(s.lengthOfLongestSubstring('bbbbb'))
    # print(s.lengthOfLongestSubstring('pwwkew'))

    print(s.nthUglyNumber(11))