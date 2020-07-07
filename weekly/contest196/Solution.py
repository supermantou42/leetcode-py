from typing import *
import time

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 2:
            return True
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2,n):
            if arr[i] - arr[i-1] != d:
                return False
        return True

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort()
        right.sort()

        while left and right:
            if left[0] < right[0]:
                left.pop(0)
            else:
                break

        while left and right:
            if left[-1] < right[-1]:
                right.pop(-1)
            else:
                break

        t = 0
        while True:
            if len(left) == 0:
                if len(right) == 0:
                    return t
                return t+n-right[0]
            if len(right) == 0:
                if len(left) == 0:
                    return t
                return t+left[-1]
            if left[-1] <= right[0]:
                return t+max(left[-1],n-right[0])

            if left[0] > right[-1] + 1:
                step = (left[0] - right[-1])//2
                t+=step
                for i in range(len(left)):
                    left[i]-=step
                for i in range(len(right)):
                    right[i]+=step

            else:
                toberight = []
                i = 1
                while i < len(left):
                    if left[i] - left[i-1] != 1:
                        toberight = left[:i]
                        left = left[i:]
                        break
                    i+=1
                if i == len(left):
                    toberight = left
                    left = []

                tobeleft = []
                i = len(right)-2
                while i >= 0:
                    if right[i+1] - right[i] != 1:
                        tobeleft = right[i+1:]
                        right = right[:i+1]
                        break
                    i-=1
                if i == -1:
                    tobeleft = right
                    right = []

                for i in range(len(left)):
                    left[i]-=1
                for i in range(len(right)):
                    right[i] += 1

                left += tobeleft
                left.sort()
                right+=toberight
                right.sort()
                if left[0] == 0:
                    left.pop(0)
                if right[-1] == n:
                    right.pop(-1)
                t+=1

        return t



    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = mat[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]
            if mat[i][0] == 1:
                dp[i][0] += 1
                for ii in range(i)[::-1]:
                    if mat[ii][0] == 1:
                        dp[i][0]+=1
                    else:
                        break
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]
            if mat[0][j] == 1:
                dp[0][j] +=1
                for jj in range(j)[::-1]:
                    if mat[0][jj] == 1:
                        dp[0][j] +=1
                    else:
                        break

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
                if mat[i][j] == 1:
                    t = j+1
                    ans = 0
                    for ii in range(i+1):
                        for jj in range(t):
                            if mat[i-ii][j-jj] == 1:
                               ans+=1
                            else:
                                t = jj
                                break
                    dp[i][j] += ans
        return dp[-1][-1]

    def minInteger(self, num: str, k: int) -> str:
        num = list(map(int,num))
        n = len(num)
        def fmin(k):
            midx = 0
            for idx in range(1,k):
                if num[idx] < num[midx]:
                    midx = idx
                    if num[idx] == 0:
                        return idx
            return midx
        ans = ''
        while k > 0:
            midx = fmin(len(num))

            if k >= midx:
               ans += str(num.pop(midx))
               k -= midx
            else:
                k2 = fmin(k+1)
                if k2 > 0:
                    ans += str(num.pop(k2))
                    k-=k2
                else:
                    prev = num[0]
                    while num and len(num) > k and num[k] >= prev:
                        ans += str(num.pop(0))
                    # for i in range(k2+1,len(num)):
                    #     if num[i] < num[0]:
                    #         ans += str(num.pop(i))
                    #         k= 0
                    #         break
                    # break
        return ans + ''.join(map(str,num))


if __name__ == '__main__':
    s = Solution()
    # print(s.numSubmat([[1,0,1],[0,1,0],[1,0,1]]))
    print(s.minInteger("294984148179",11))