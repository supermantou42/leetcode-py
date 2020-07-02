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

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 当作n个队列，每次取最小，出队，第k个出队的即为答案 O(n*k)
        # n = len(matrix)
        # if n == 0:
        #     return 0
        # # cnt = 0
        # ans = -1
        # idxs = [0] * n
        # for i in range(k):
        #     idj = -1
        #     for j in range(n):
        #         if idxs[j] < n:
        #             idj = j
        #             break
        #
        #     for j in range(n):
        #         if idxs[j] < n and matrix[j][idxs[j]] < matrix[idj][idxs[idj]]:
        #             idj = j
        #     ans = matrix[idj][idxs[idj]]
        #     idxs[idj] += 1
        #     # cnt+=1
        # return ans
        # 用堆来包装队列(用下标代替指针) O(klogn)
        # import heapq
        # n = len(matrix)
        # if n == 0:
        #     return 0
        # pq = [(matrix[i][0],i,0) for i in range(n)]
        # heapq.heapify(pq)
        # for k in range(k-1):
        #     _, x, y = heapq.heappop(pq)
        #     if y < n - 1:
        #         heapq.heappush(pq,(matrix[x][y+1],x,y+1))
        # return heapq.heappop(pq)[0]

        # 二分 O(nlog(max-min))
        n = len(matrix)
        if n == 0:
            return 0
        def check(v):
            i,j = n-1,0
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= v:
                    cnt += i+1
                    j+=1

                else:
                    i-=1

            return cnt

        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            m = (l+r)//2
            v = check(m)
            if v < k:
                l = m + 1
            else:  # 在第k小和k+1小中间的值都取等，不能取等时返回
                r = m
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest(matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,))