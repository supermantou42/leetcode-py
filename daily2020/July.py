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

    # 8th
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        ans = []
        if shorter == longer:
            return [shorter*k]
        v = shorter * k
        d = longer - shorter
        ans.append(v)
        for i in range(1,k):
            v += d
            ans.append(v)
        return ans

    # 9th
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trietree = {}
        for words in dictionary:
            t = trietree
            for char in words[:0:-1]:
                if char not in t:
                    t[char] = {}
                t = t[char]
            if words[0] not in t:
                t[words[0]] = {None:"end"}
            else:
                t[words[0]][None] = "end"

        n = len(sentence)
        dp = list(range(n+1))

        for i in range(1,n+1):
            Flag = True
            t = trietree
            for j in range(1,i+1)[::-1]:
                dp[i] = min(dp[i], dp[j-1] + i - j + 1)
                if sentence[j-1] not in t:
                    Flag = False
                    break
                else:
                    if None in t[sentence[j-1]]:
                        dp[i] = min(dp[i], dp[j-1])
                        if len(t[sentence[j-1]]) == 1:
                            Flag = False
                            break
                    t = t[sentence[j-1]]
            if Flag and None in t:
                dp[i] = 0

        return dp[-1]

    #10th
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 0 冷冻且不持有 1 冷冻持有 2 不持有不冷冻
        dp = [[0,0,0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][1] + prices[i]
            dp[i][1] = max(dp[i-1][1], dp[i-1][2] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][0])

        return max(dp[-1])
    # 11st
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        dnums = sorted(set(nums))
        nums2idx = {num:idx+1 for idx,num in enumerate(dnums)}
        dn = len(dnums)+1
        nums = [nums2idx[num] for num in nums]
        bit = BIT(dn)
        ans = [0] * n
        bit.update(nums[-1])
        for i in range(n-1)[::-1]:
            ans[i] = bit.query(nums[i]-1) # -1 表示不能取等
            bit.update(nums[i])
        return ans

    # 12nd
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # DFS 超时
        # m = len(dungeon)
        # n = len(dungeon[0])
        # ans = [-10**9]
        # def dfs(i,j,cur,hismin):
        #     cur += dungeon[i][j]
        #     hismin = min(hismin,cur)
        #     if i == m-1 and j == n-1:
        #         ans[0] = max(ans[0], hismin)
        #     if hismin > ans[0]:
        #         if i < m - 1:
        #             dfs(i+1,j,cur,hismin)
        #         if j < n - 1:
        #             dfs(i,j+1,cur,hismin)
        # dfs(0,0,0,10**9)
        # return max(1-ans[-1],1)
        # DP
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = max(-dungeon[-1][-1]+1, 1)
        for i in range(m-1)[::-1]:
            dp[i][-1] = max(dp[i+1][-1] - dungeon[i][-1],1)
        for j in range(n-1)[::-1]:
            dp[-1][j] = max(dp[-1][j+1] - dungeon[-1][j],1)
        for i in range(m-1)[::-1]:
            for j in range(n-1)[::-1]:
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

        return dp[0][0]

    #13rd
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 通用-集合操作
        # import collections
        # n1 = collections.Counter(nums1)
        # n2 = collections.Counter(nums2)
        # sharekey = n1.keys() & n2.keys()
        # ans = []
        # for key in sharekey:
        #     ans += [key] * min(n1[key],n2[key])
        # return ans
        # 通用-查表操作
        import collections
        n1 = collections.Counter(nums1)
        ans = []
        for n in nums2:
            if n1[n] > 0:
                ans.append(n)
                n1[n]-=1
        return ans
        # 排序
        # nums1.sort()
        # nums2.sort()
        # ans = []
        # n = len(nums1)
        # m = len(nums2)
        # i,j = 0,0
        # while i < n and j < m:
        #     if nums1[i] == nums2[j]:
        #         ans.append(nums1[i])
        #         i+=1
        #         j+=1
        #     elif nums1[i] < nums2[j]:
        #         i+=1
        #     else:
        #         j+=1
        # return ans

    # 14th
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(1, i)[::-1]:
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)

        # ans = [10**9+7]
        # ref = [min(nn) for nn in triangle]
        # for i in range(n-1)[::-1]:
        #     ref[i] += ref[i+1]

        # def dfs(depth,i,total):
        #     if depth == n:
        #         ans[0] = min(ans[0],total)
        #         return
        #     if total + ref[depth] > ans[0]:
        #         return
        #     total+=triangle[depth][i]
        #     dfs(depth+1,i,total)
        #     dfs(depth+1,i+1,total)
        # dfs(0,0,0)
        # return ans[0]

    # 15th
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = 0
            for j in range(i//2):
                dp[i] += 2*dp[j]*dp[i-j-1]
            if i % 2 == 1:
                dp[i] += dp[i//2]**2
        return dp[-1]

    # 16th
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 广度优先
        # n = len(graph)
        # color = [0]*n
        # i = 0
        # cnt = 0
        # while i < n and cnt < n:
        #     if color[i] == 0 and graph[i]:
        #         color[i] = 1
        #         cnt+=1
        #         nowcolor = -1
        #         nowset = {i}
        #         while nowset:
        #             nextset = set()
        #             for ii in nowset:
        #                 for j in graph[ii]:
        #                     if color[j] != 0 and color[j] != nowcolor:
        #                         return False
        #                     if color[j] == 0:
        #                         cnt+=1
        #                         color[j] = nowcolor
        #                         nextset.add(j)
        #             nowcolor = -nowcolor
        #             nowset = nextset
        #     i+=1
        # return True
        # 并查集
        n = len(graph)
        uf = UnionFind(n)
        for i,g in enumerate(graph):
            if g:
                g0 = g[0]
                for gg in g[1:]:
                    if uf.isconneted(i,gg):
                        return False
                    uf.union(g0,gg)
        return True

    # 17th
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n
        while l<r:
            mid = (l+r) //2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        return l

    # 18th
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 时O(n^2)空O(n^2)
        # m = len(s1)
        # n = len(s2)
        # if m+n != len(s3):
        #     return False
        # dp = [[False]*(n+1) for _ in range(m+1)]
        # dp[0][0] = True
        # for i in range(1,m+1):
        #     if dp[i-1][0] and s1[i-1] == s3[i-1]:
        #         dp[i][0] = True
        #     else:
        #         break
        # for j in range(1,n+1):
        #     if dp[0][j-1] and s2[j-1] == s3[j-1]:
        #         dp[0][j] = True
        #     else:
        #         break
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) \
        #                    or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        #
        # return dp[-1][-1]
        # 空优化O(n)
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        dp = [False]*(n+1)
        dp[0] = True
        for j in range(1,n+1):
            if dp[j-1] and s2[j-1] == s3[j-1]:
                dp[j] = True
            else:
                break

        for i in range(1,m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1,n+1):
                dp[j] = (s1[i-1] == s3[i+j-1] and dp[j]) \
                           or (s2[j-1] == s3[i+j-1] and dp[j-1])

        return dp[-1]

    # 19th
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for i in range(n-3,-1,-1):
            for j in range(i+2,n):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[0][n-1]

    #20th
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i,j = 0,n-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i,j]
            elif numbers[i]+numbers[j] > target:
                j-=1
            else:
                i+=1
        return [-1,-1]

    # 21st
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen(start,end):
            if start == end:
                return [None]
            if start + 1 == end:
                return [TreeNode(start)]
            # mid = (start+end)//2
            ans = []
            for m in range(start,end):
                left = gen(start,m)
                right = gen(m+1,end)
                for l in left:
                    for r in right:
                        node = TreeNode(m)
                        node.left = l
                        node.right = r
                        ans.append(node)
            return ans
        return gen(1,n+1)

    #22nd
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            if numbers[l] < numbers[r]:
                return numbers[l]
            m = (l+r)//2
            if numbers[m] < numbers[m-1]:
                return numbers[m]
            if numbers[m] < numbers[r]:
                r = m
            elif numbers[m] > numbers[r]:
                l = m + 1
            else:
                r -= 1
        return numbers[l]

    # 23rd
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    # 24th
    def divisorGame(self, N: int) -> bool:
        return N%2==0

    # 25th
    def splitArray(self, nums: List[int], m: int) -> int:
        # DP
        # n = len(nums)
        # subsum = nums.copy()
        # for i in range(1,n):
        #     subsum[i]+=subsum[i-1]
        # dp = [[10**9]*n for _ in range(m)]
        # dp[0][0] = nums[0]
        # for j in range(1,n):
        #     dp[0][j] = dp[0][j-1] + nums[j]
        # for i in range(1,m):
        #     dp[i][i] = max(dp[i-1][i-1], nums[i])
        #     for j in range(i+1,n):
        #         for k in range(i-1,j):
        #             dp[i][j] = min(dp[i][j],max(dp[i-1][k], subsum[j] - subsum[k]))
        #
        # return dp[-1][-1]
        # 二分
        n = len(nums)
        l,r = max(nums),sum(nums)
        if m == 1:
            return r
        while l < r:
            mid = (l+r)//2
            cnt = 1
            partsum = 0
            for i in range(n):
                if partsum+nums[i] > mid:
                   cnt += 1
                   partsum = nums[i]
                else:
                    partsum+=nums[i]
            if cnt > m:
                l = mid + 1
            else:
                r = mid
        return l

    # 26th
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        mem = [[0]*n for _ in range(m)]
        visted = [[0]*n for _ in range(m)]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(x,y):
            if mem[x][y] > 0:
                return mem[x][y]
            v = matrix[x][y]
            visted[x][y] = 1
            depth = 0
            for d in dirs:
                xx,yy = x+d[0],y+d[1]
                if xx<0 or xx >=m or yy <0 or yy >= n:
                    continue
                if matrix[xx][yy] > v:
                    depth = max(depth, dfs(xx,yy))
            mem[x][y] = depth+1
            visted[x][y] = 0
            return depth+1

        for i in range(m):
            for j in range(n):
                mem[i][j] = dfs(i,j)
        return max(map(max,mem))
    #27th
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i,j = 0,0
        while i < m and j < n:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i == m
    #28th
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        def dfs(node: TreeNode,depth:int):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.depth = max(self.depth, depth+1)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return self.depth
    # 29th
    def minimalSteps(self, maze: List[str]) -> int:
        # 四个方向
        dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # 计算（x, y）到maze中其他点的距离，结果保存在ret中
        def bfs(x, y, maze, m, n):
            ret = [[-1] * n for _ in range(m)]
            ret[x][y] = 0
            q = Queue()
            q.put((x, y))
            while q.qsize():
                curx, cury = q.get()
                for dx, dy in dd:
                    nx = curx + dx
                    ny = cury + dy
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '#' and ret[nx][ny] == -1:
                        ret[nx][ny] = ret[curx][cury] + 1
                        q.put((nx, ny))
            return ret

        m = len(maze)
        n = len(maze[0])

        startX = -1
        startY = -1
        endX = -1
        endY = -1

        # 机关 & 石头
        buttons = []
        stones = []

        # 记录所有特殊信息的位置
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    startX = i
                    startY = j
                elif maze[i][j] == 'T':
                    endX = i
                    endY = j
                elif maze[i][j] == 'O':
                    stones.append((i, j))
                elif maze[i][j] == 'M':
                    buttons.append((i, j))
                else:
                    pass

        nb = len(buttons)
        ns = len(stones)

        startToAnyPos = bfs(startX, startY, maze, m, n)

        # 若没有机关，最短距离就是(startX, startY)到(endX, endY)的距离
        if nb == 0:
            return startToAnyPos[endX][endY]

        # 记录第i个机关到第j个机关的最短距离
        # dist[i][nb]表示到起点的距离， dist[i][nb+1]表示到终点的距离
        dist = [[-1] * (nb + 2) for _ in range(nb)]

        # 遍历所有机关，计算其和其他点的距离
        buttonsToAnyPos = []
        for i in range(nb):
            bx, by = buttons[i]
            # 记录第i个机关到其他点的距离
            iToAnyPos = bfs(bx, by, maze, m, n)
            buttonsToAnyPos.append(iToAnyPos)
            # 第i个机关到终点的距离就是(bx, by)到(endX, endY)的距离
            dist[i][nb + 1] = iToAnyPos[endX][endY]

        for i in range(nb):
            # 计算第i个机关到(startX, startY)的距离
            # 即从第i个机关出发，通过每个石头(sx, sy)，到(startX, startY)的最短距离
            tmp = -1
            for j in range(ns):
                sx, sy = stones[j]
                if buttonsToAnyPos[i][sx][sy] != -1 and startToAnyPos[sx][sy] != -1:
                    if tmp == -1 or tmp > buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]:
                        tmp = buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]

            dist[i][nb] = tmp

            # 计算第i个机关到第j个机关的距离
            # 即从第i个机关出发，通过每个石头(sx, sy)，到第j个机关的最短距离
            for j in range(i + 1, nb):
                mn = -1
                for k in range(ns):
                    sx, sy = stones[k]
                    if buttonsToAnyPos[i][sx][sy] != -1 and buttonsToAnyPos[j][sx][sy] != -1:
                        if mn == -1 or mn > buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]:
                            mn = buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]
                # 距离是无向图，对称的
                dist[i][j] = mn
                dist[j][i] = mn

        # 若有任意一个机关 到起点或终点没有路径(即为-1),则说明无法达成，返回-1
        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb + 1] == -1:
                return -1

        # dp数组， -1代表没有遍历到, 1<<nb表示题解中提到的mask, dp[mask][j]表示当前处于第j个机关，总的触发状态为mask所需要的最短路径, 由于有2**nb个状态，因此1<<nb的开销必不可少
        dp = [[-1] * nb for _ in range(1 << nb)]
        # 初识状态，即从start到第i个机关，此时mask的第i位为1，其余位为0
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]

        # 二进制中数字大的mask的状态肯定比数字小的mask的状态多，所以直接从小到大遍历更新即可
        for mask in range(1, (1 << nb)):
            for i in range(nb):
                # 若当前位置是正确的，即mask的第i位是1
                if mask & (1 << i) != 0:
                    for j in range(nb):
                        # 选择下一个机关j,要使得机关j目前没有到达，即mask的第j位是0
                        if mask & (1 << j) == 0:
                            nextMask = mask | (1 << j)
                            if dp[nextMask][j] == -1 or dp[nextMask][j] > dp[mask][i] + dist[i][j]:
                                dp[nextMask][j] = dp[mask][i] + dist[i][j]

        # 最后一个机关到终点
        ans = -1
        finalMask = (1 << nb) - 1
        for i in range(nb):
            if ans == -1 or ans > dp[finalMask][i] + dist[i][nb + 1]:
                ans = dp[finalMask][i] + dist[i][nb + 1]
        return ans
    # 30nd
    def integerBreak(self, n: int) -> int:
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return ans * n

    #31st
    def findMagicIndex(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                return i
            if nums[i] > i:
                i = nums[i]
            else:
                i+=1
        return -1

class UnionFind:
    def __init__(self,n):
        self.values = list(range(n))

    def union(self, p, q):
        if p == q:
            return
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return
        self.values[rp] = rq

    def find(self, x):
        if x == self.values[x]:
            return x
        x = self.find(self.values[x])
        return x

    def isconneted(self,p,q):
        if p == q:
            return True
        rp = self.find(p)
        rq = self.find(q)
        return rp == rq


class BIT:
    def __init__(self,n):
        self.data = [0]*n
        self.n = n
    def lowbit(self,x):
        return x & (-x)

    def query(self,idx):
        ans = 0
        while idx>0:
            ans += self.data[idx]
            idx -= self.lowbit(idx)
        return ans

    def rangesum(self,l,r):
        if l == 0:
            return self.query(r)
        else:
            return self.query(r) - self.query(l-1)

    def update(self,x,v=1):
        while x < self.n:
            self.data[x]+=v
            x+=self.lowbit(x)

if __name__ == '__main__':
    s = Solution()
    # print(s.isMatch("a", "a**"))
#     print(s.respace(["reqpqsspxepbblebeqcx","iapuwgpglww","lee","r","ra","mecb","x","w","pwurqagwecsxeuqxgc","b"]
# ,"cwpilmxbulaql"))
#     print(s.countSmaller([5,2,6,1]))
#     print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
#     print(s.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))
#     print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
#     print(s.searchInsert([1,3,5,6], 5))
#     print(s.isInterleave(s1 = "a", s2 = "", s3 = "a"))
#     print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
#     print(s.maxCoins([3,1,5,8]))
#     print(s.splitArray([7,2,5,10,8],2))
#     print(s.isSubsequence("axc", "ahbgdc"))
    print(s.findMagicIndex([1, 1, 1]))