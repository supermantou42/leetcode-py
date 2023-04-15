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
        right = [n-r for r in right]
        return max(left+right)


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
        numtable = [[] for _ in range(10)]
        for i in range(n):
            numtable[num[i]].append(i)

        ancnt = [0]
        def fmin(x,v,k):
            flag = False
            idx, ret = -1,-1
            for idx in range(v):
                if numtable[idx] and numtable[idx][0] - x - ancnt[0] <=k:
                    ret = numtable[idx][0]
                    numtable[idx].pop(0)
                    flag = True
                    break
            if flag:
                 for i in range(10):
                     if numtable[i]:
                         for j in range(len(numtable[i])):
                             if numtable[i][j] < ret:
                                 numtable[i][j] += 1

                 ancnt[0]+=1
            return idx,ret - x - ancnt[0]

        ans = ''
        i = 0
        while k > 0 and i < n:
            dx,dk = fmin(i,num[i],k)
            if dx == -1:
                v = num[i]
                ans += str(v)
                numtable[v].pop(0)
                i += 1
            else:
                ans += str(dx)
                k -= dk
        while True:
            idx = -1
            j = -1
            while j < 10:
                if numtable[j]:
                    idx = j
                    break
                j+=1
            if idx == -1:
                break
            while j < 10:
                if numtable[j] and numtable[j][0] < numtable[idx][0]:
                    idx = j
                j+=1

            numtable[idx].pop(0)
            ans += str(idx)
        return ans








if __name__ == '__main__':
    s = Solution()
    # print(s.numSubmat([[1,0,1],[0,1,0],[1,0,1]]))
    # print(s.minInteger("4321",4))
    # print(s.minInteger("294984148179",11))
    print(s.minInteger("9438957234785635408", 23))