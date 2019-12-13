from typing import *
import time


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        total = 0
        for p in points[1:]:
            total += max(abs(p[0] - prev[0]), abs(p[1] - prev[1]))
            prev = p
        return total

    def countServers(self, grid: List[List[int]]) -> int:
        total = 0
        row_cnt = [[] for _ in range(len(grid))]
        col_cnt = [[] for _ in range(len(grid[0]))]
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    total += 1
                    row_cnt[i].append(j)
                    col_cnt[j].append(i)
        for i, r in enumerate(row_cnt):
            if len(r) == 1 and len(col_cnt[r[0]]) == 1:
                total -= 1
        return total

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefix = ''
        ans = []
        for sw in searchWord:
            products = sorted(list(filter(lambda x: x.startswith(sw), products)))
            t = []
            for p in products[:3]:
                t.append(prefix + p)
            ans.append(t)
            prefix += sw
            temp = []
            for p in products:
                if len(p) > 1:
                    temp.append(p[1:])
            products = temp
        return ans

    def numWays(self, steps: int, arrLen: int) -> int:
        # from scipy.special import comb
        # table = [1, 0]
        #
        # def go(remain_steps, ind):
        #     if ind < 0 or ind == arrLen:
        #         return 0
        #     if ind > remain_steps:
        #         return 0
        #     if ind == remain_steps:
        #         return 1
        #     if ind == 0 and remain_steps < len(table):
        #         return table[remain_steps]
        #     return go(remain_steps - 1, ind - 1) + go(remain_steps - 1, ind + 1)
        #
        # for i in range(2,steps + 1):
        #     if i % 2 == 1:
        #         table.append(0)
        #     else:
        #         if i // 2 > arrLen - 1:
        #             table.append(go(i, 0))
        #         else:
        #             table.append(int(comb(i,i//2))//2)
        # for i in range(len(table)):
        #     table[i] *= int(comb(steps, i))
        # return sum(table) % (10 ** 9 + 7)
        mxr = min(steps // 2 + 1, arrLen)
        prev = [0] * (mxr + 2)
        prev[1] = 1
        now = [0] * (mxr + 2)
        for i in range(steps):
            for j in range(1,mxr+1):
                now[j] = sum(prev[j-1:j+2])
            prev = now
            now = [0] * (mxr + 2)
        return prev[1] % (10**9+7)


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(steps = 3, arrLen = 2))
    print(s.numWays(steps = 2, arrLen = 4))
    print(s.numWays(steps = 4, arrLen = 2))
    import time
    start = time.time()
    print(s.numWays(steps = 47, arrLen = 38))
    print((time.time() - start))