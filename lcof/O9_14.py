from typing import *


class CQueue:

    def __init__(self):
        self.qa = []
        self.qb = []
        self.len = 0

    def appendTail(self, value: int) -> None:
        # if self.qb:
        #     self.qa += self.qb[::-1]
        #     self.qb.clear()
        self.qa.append(value)
        self.len += 1

    def deleteHead(self) -> int:
        if self.len == 0:
            return -1
        if not self.qb:
            self.qb += self.qa[::-1]
            self.qa.clear()
        self.len -= 1
        return self.qb.pop(-1)


class Solution:
    def fib(self, n: int) -> int:
        # 递归法
        # if n <= 1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        # 查表
        if n <= 1:
            return n
        table = [0] * (n + 1)
        table[1] = 1
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[-1] % 1000000007

    def numWays(self, n: int) -> int:
        # 递归版本
        # if n <= 1:
        #     return 1
        # return self.numWays(n-1)+self.numWays(n-2)
        # 查表
        if n <= 1:
            return 1
        table = [1] * (n + 1)
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[-1] % 1000000007

    def minArray(self, numbers: List[int]) -> int:
        # # 顺序查 O(n)
        # n = len(numbers)
        # if numbers[0] < numbers[-1]:
        #     return numbers[0]
        # for i in range(1,n):
        #     if numbers[i] < numbers[i-1]:
        #         return numbers[i]
        # return numbers[0]

        # 二分 O(logn)
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            if numbers[l] < numbers[r]:
                return numbers[l]
            m = (l + r) // 2
            if numbers[m] < numbers[m - 1]:
                return numbers[m]
            if numbers[m] < numbers[r]:
                r = m
            elif numbers[m] > numbers[r]:
                l = m + 1
            else:
                r -= 1
        return numbers[l]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        # visit = [[False] * n for _ in range(m)]
        dirs = (
            (0, -1), (0, 1), (-1, 0), (1, 0),
                )

        def dfs(x, y, i):
            if i == l - 1:
                if board[x][y] == word[i]:
                    return True
                else:
                    return False
            if board[x][y] != word[i]:
                return False

            board[x][y] = "@"
            for d in dirs:
                xx, yy = x + d[0], y + d[1]
                if xx < 0 or xx >= m or yy < 0 or yy >= n:
                    continue
                if dfs(xx,yy, i + 1):
                    return True
            board[x][y] = word[i]
            return False

        for xx in range(m):
            for yy in range(n):
                if board[xx][yy] == word[0] and dfs(xx, yy, 0):
                    return True
        return False

    def movingCount(self, m: int, n: int, k: int) -> int:
        # cnt = 0
        visited = [[False]*n for _ in range(m)]
        dirs = (
            (0, -1), (0, 1), (-1, 0), (1, 0),
                )
        def getnumbersum(n):
            a = 0
            while n > 0:
                a += n % 10
                n //= 10

            return a

        def dfs(x,y):
            visited[x][y] = True
            cnt = 1
            for dx,dy in dirs:
                xx, yy = x+dx,y+dy
                if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy] \
                        and getnumbersum(xx) + getnumbersum(yy) <= k:
                   cnt += dfs(xx,yy)
            return cnt

        ans = dfs(0,0)
        return ans

    def cuttingRope(self, n: int) -> int:
        import math
        if n < 4:
            return n - 1

        s = int(math.pow(3,(n // 3 - 1)))
        m = [3,4,6]
        s *= m[n%3]

        return s

if __name__ == '__main__':
    # obj = CQueue()
    # obj.appendTail(3)
    # print(obj.deleteHead())
    # print(obj.deleteHead())
    # print(obj.deleteHead())
    s = Solution()
    # print(s.exist([["a","b"],["c","d"]],"cdba"))
    print(s.cuttingRope(36))