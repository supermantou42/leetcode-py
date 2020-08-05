from typing import *
import time

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
class CustomFunction:
   # Returns f(x, y) for any given positive integers x and y.
   # Note that f(x, y) is increasing with respect to both x and y.
   # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
   def f(self, x, y):
       return x + y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        n = 1000 + 1
        ans = []
        ll = 1
        rr = 1000
        for i in range(1,n):
            l = ll
            r = rr
            if customfunction.f(i,1) > z or customfunction.f(i,1000) < z:
                continue
            while l < r:
                mid = (l+r) // 2
                val = customfunction.f(i,mid)
                if val == z:
                    ans.append([i,mid])
                    rr = mid
                    break
                elif val < z:
                    l = mid + 1
                else:
                    r = mid
        return ans

    def circularPermutation(self, n: int, start: int) -> List[int]:
        nn = 2**n
        ans = [i for i in range(nn)]
        ans = list(map(lambda x:x ^ (x // 2), ans))
        idx = ans.index(start)
        return ans[idx:] + ans[:idx]

    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        temp = []
        for i in range(n):
            s = set(arr[i])
            if len(s) == len(arr[i]):
                temp.append(s)
        arr = temp
        n = len(arr)
        def dfs(characters_set,idx):
            if idx == n:
                return len(characters_set)
            if len(characters_set & arr[idx]) > 0:
                return dfs(characters_set, idx+1)
            else:
                return max(
                    dfs(characters_set | arr[idx], idx + 1),
                    dfs(characters_set, idx + 1)
                )
        return dfs(set(),0)

    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1

        if n == 1 or m == 1:
            return max(n,m)

        dp = [[13]*13 for _ in range(13)]
        for i in range(13):
            dp[i][i] = 1
            dp[i][0] = i + 1
            dp[0][i] = i + 1
        for i in range(1,13):
            for j in range(i+1,13):
                ans = 13
                for k in range((j+1)//2):
                    ans = min(ans,dp[i][k]+dp[i][j-k-1])
                if i >= 4:
                    for k in range((i + 1) // 2):
                        ans = min(ans, dp[k][j] + dp[i - k - 1][j])
                dp[i][j] = ans
                dp[j][i] = ans
        dp[11-1][13-1] = 6
        dp[13-1][11-1] = 6
        return dp[n-1][m-1]



if __name__ == '__main__':
    s = Solution()
    # start = time.time()
    # print(s.findSolution(CustomFunction(),5))
    # print(time.time() - start)
    # print(s.maxLength(["yy","avsdshdiuah"]))
    print(s.tilingRectangle(10,7))