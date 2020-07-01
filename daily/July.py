from typing import *


class Solution:
    # 1st
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        if n == 0 or m == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        if A[-1] == B[-1]:
            dp[-1][-1] = 1
        for i in range(m-1)[::-1]:
            if A[i] == B[-1]:
                dp[i][-1] = 1
            # else:
            #     dp[i][-1] = 0
        for j in range(n-1)[::-1]:
            if A[-1] == B[j]:
                dp[-1][j] = 1
        ans = 0
        for i in range(m-1)[::-1]:
            for j in range(n-1)[::-1]:
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    ans = max(ans,dp[i][j])
                # else:
                #     dp[i][j] = 0
        return ans