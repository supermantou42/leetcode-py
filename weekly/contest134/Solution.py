from typing import *


class Solution(object):
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        if grid[r0][c0] != color:
            m = len(grid)
            n = len(grid[0])
            visit = [[0] * n for _ in range(m)]  # 0表示未访问 1表示已访问的内部结点，-1表示已访问的外部结点
            self.go(grid, r0, c0, visit, grid[r0][c0], color)
        return grid

    def go(self, grid, rn, cn, visit, from_color, to_color):
        m = len(grid)
        n = len(grid[0])
        if 0 <= rn < m and 0 <= cn < n:
            if visit[rn][cn] == 0:
                if grid[rn][cn] == from_color:
                    visit[rn][cn] = 1
                    ans = [self.go(grid, rn - 1, cn, visit, from_color, to_color),
                           self.go(grid, rn, cn + 1, visit, from_color, to_color),
                           self.go(grid, rn + 1, cn, visit, from_color, to_color),
                           self.go(grid, rn, cn - 1, visit, from_color, to_color)]
                    if ans.count(-1) > 0:
                        grid[rn][cn] = to_color
                else:
                    visit[rn][cn] = -1
                return visit[rn][cn]
            else:
                return visit[rn][cn]
        else:
            return -1

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        d = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        return d[m - 1][n - 1]




if __name__ == "__main__":
    # grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    s = Solution()
    # print(s.colorBorder(grid, 1, 1, 2))
    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    print(s.maxUncrossedLines(A, B))
