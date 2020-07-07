from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    # 2nd
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
    # 3rd
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def go(l,r):
            if l == r:
                return None
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = go(l,m)
            node.right = go(m+1,r)
            return node
        n = len(nums)
        return go(0,n)
    # 4th
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        dp = [0] *n
        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
        for i in range(2,n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2
                else:
                    if i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + 2
                        if i-dp[i-1]-2 >= 0:
                            dp[i] += dp[i-dp[i-1]-2] # 消除非法括号后，可以和前面的拼接起来
        return dp[-1]

    # 5th
    def isMatch(self, s: str, p: str) -> bool:
        # 分支递归，超时
        # m = len(s)
        # n = len(p)
        #
        # if n == 0:
        #     return m == 0
        # # delete redundant *
        # pp = [p[0]]
        # for i in range(1,n):
        #     if p[i] == '*' and p[i-1] == '*':
        #         continue
        #     pp.append(p[i])
        # n = len(pp)
        # p = pp
        # def go(i,j):
        #     if i == m:
        #         if j < n:
        #             if j == n - 1 and p[j] == '*':
        #                 return True
        #             return False
        #         return True
        #     if j == n:
        #         return False
        #     if p[j] == '?':
        #         return go(i+1,j+1)
        #     elif p[j] == '*':
        #         return go(i+1,j+1) or go(i+1,j) or go(i,j+1)
        #     else:
        #         if s[i] != p[j]:
        #             return False
        #         return go(i+1,j+1)
        #
        # return go(0,0)
        m = len(s)
        n = len(p)

        if n == 0:
            return m == 0
        # delete redundant *
        pp = [p[0]]
        for i in range(1,n):
            if p[i] == '*' and p[i-1] == '*':
                continue
            pp.append(p[i])
        n = len(pp)
        p = pp

        if m == 0:
            return p[0] == '*' and len(p) == 1

        if p[0] == '*':
            s = '?' + s
            m+=1
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = s[0] == p[0] or p[0] == '?' or p[0] == '*'
        if p[0] == '*':
            for i in range(1,m):
                dp[i][0] = True
        if dp[0][0] and n > 1 and p[1] == '*':
            dp[0][1] = True

        for i in range(1,m):
            for j in range(1,n):
                if p[j] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] # dp[i-1][j-1] 被包含在dp[i-1][j]中
                else:
                    dp[i][j] = s[i] == p[j] and dp[i-1][j-1]

        return dp[-1][-1]

    #6th
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1:
            return 0 if 1 in obstacleGrid[0] else 1
        if n == 1:
            return 0 if [1] in obstacleGrid else 1

        prev = [1]*m
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for ii in range(i,m):
                    prev[ii] = 0
                break

        now = [1] if obstacleGrid[0][0] == 0 else [0]
        for j in range(1,n):
            now = [1] if now[0] == 1 and obstacleGrid[0][j] == 0 else [0]
            for i in range(1,m):
                if obstacleGrid[i][j] == 0:
                    now.append(now[-1]+prev[i])
                else:
                    now.append(0)
            prev = now
        return prev[-1]

    #7th
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def go(node, res):
            if node is None:
                return False
            res -= node.val
            if res == 0:
                if node.left is None and node.right is None:
                    return True
            return go(node.left, res) or go(node.right, res)
        return go(root,sum)


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("a", "a**"))