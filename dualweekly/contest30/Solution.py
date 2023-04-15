from typing import *

class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05'
                    , "Jun":'06', "Jul":'07', "Aug":'08',
                 "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        d,m,y = date.split(' ')
        d = d[:-2]
        m = month[m]
        return f"{y}-{m}-{d}"

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        table = [[]for _ in range(n)]
        table[0] = nums.copy()
        for i in range(1,n):
            for j in range(n-i):
                table[i].append(table[i-1][j]+nums[i+j])
        t = table[0]
        for i in range(1,n):
            t+=table[i]
        t.sort()
        return sum(t[left-1:right]) % (10**9 + 7)

    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        return min([nums[n-4+i] - nums[i] for i in range(4)])

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        dp[1] = True
        for i in range(1,n+1):
            j = 1
            while j**2 <= i:
                if not dp[i-j**2]:
                    dp[i] = True
                    break
                j+=1
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))
    # print(s.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4))
    # print(s.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10))
    # print(s.minDifference([5,3,2,4]))
    # print(s.minDifference([1,5,0,10,14]))
    # print(s.minDifference([6,6,0,1,1,4,6]))
    # print(s.minDifference( [1,5,6,14,15]))
    print(s.winnerSquareGame(1))
    print(s.winnerSquareGame(2))
    print(s.winnerSquareGame(4))
    print(s.winnerSquareGame(7))
    print(s.winnerSquareGame(17))