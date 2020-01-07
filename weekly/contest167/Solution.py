from typing import *
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head is not None:
            ans = ans * 2 + head.val
            head = head.next
        return ans

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sl = len(str(low))
        el = len(str(high - 1))
        ans = []
        for l in range(sl, el + 1):
            for i in range(1, 10 - l + 1):
                a = 0
                for j in range(l):
                    a = a * 10 + i + j
                if low <= a <= high:
                    ans.append(a)
        return ans

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        msl = min(m, n)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = mat[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + mat[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + mat[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = mat[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        def go(l):
            if l == 0:
                return True
            if l > msl:
                return False
            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    lt = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    lv = dp[i - 1][j + l - 1] if i > 0 else 0
                    tv = dp[i + l - 1][j - 1] if j > 0 else 0

                    s = dp[i + l - 1][j + l - 1] - lv - tv + lt
                    if s <= threshold:
                        return True
            return False

        l = 0
        r = msl + 1
        while l < r:
            mid = (l + r) // 2
            if go(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

    def shortestPath(self, grid: List[List[int]], k: int) -> int:


        # # import queue
        import collections

        m = len(grid)
        n = len(grid[0])
        k = min(k, m + n - 3)

        q = collections.deque()
        # q.put_nowait((0, 0, k))  # x,y,k
        q.append((0, 0, k))  # x,y,k
        visited = set()
        visited.add((0, 0, k))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        deep = -1
        while len(q) > 0:
            deep += 1
            for _ in range(len(q)):
                now = q.popleft()
                if now[0] == m - 1 and now[1] == n - 1:
                    return deep
                for d in dirs:
                    nx,ny = (now[0] + d[0], now[1] + d[1])
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0:
                            next_state = (nx, ny, now[2])
                        else:
                            if now[2] > 0:
                                next_state = (nx, ny, now[2] - 1)
                            else:
                                continue
                        if next_state not in visited:
                            q.append(next_state)
                            visited.add(next_state)

        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.sequentialDigits(100,300))
    # print(s.sequentialDigits(1000,13000))

    # print(s.maxSideLength(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], threshold=4))
    # print(s.maxSideLength(mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],
    #                       threshold=1))
    # print(s.maxSideLength(mat=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], threshold=6))
    # print(s.maxSideLength(mat=[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]], threshold=40184))
    # print(s.shortestPath(grid=
    #                      [[0, 0, 0],
    #                       [1, 1, 0],
    #                       [0, 0, 0],
    #                       [0, 1, 1],
    #                       [0, 0, 0]],
    #                      k=1))
    # print(s.shortestPath(grid=
    #                      [[0, 1, 1],
    #                       [1, 1, 1],
    #                       [1, 0, 0]],
    #                      k=1))
    st = time.time()
    print(s.shortestPath(
        [[0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
         [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
         [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
        , 178))
    print(time.time() - st)
