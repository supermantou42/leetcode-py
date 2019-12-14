from typing import *


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        nc = [0] * n
        mc = [0] * m
        for i in indices:
            nc[i[0]] += 1
            mc[i[1]] += 1
        ans = 0
        for nn in nc:
            for mm in mc:
                ans += (nn + mm) % 2
        return ans

    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        # dfs超时
        # n = len(colsum)
        # def dfs(deep,res,up,down):
        #     if deep == n:
        #         if up == down == 0:
        #             return res
        #         else:
        #             return []
        #     if colsum[deep] == 0:
        #         res[0].append(0)
        #         res[1].append(0)
        #         return dfs(deep+1,res,up,down)
        #     elif colsum[deep] == 2:
        #         if up == 0 or down == 0:
        #             return []
        #         else:
        #             res[0].append(1)
        #             res[1].append(1)
        #             return dfs(deep+1,res,up-1,down-1)
        #     else:
        #         a = []
        #         if up > 0:
        #             r = [res[0].copy(),res[1].copy()]
        #             r[0].append(1)
        #             r[1].append(0)
        #             a = dfs(deep+1,r,up-1,down)
        #         if len(a) > 0:
        #             return a
        #         else:
        #             if down > 0:
        #                 res[0].append(0)
        #                 res[1].append(1)
        #                 return dfs(deep + 1, res, up, down - 1)
        #             else:
        #                 return []
        # return dfs(0,[[],[]],upper,lower)
        n = len(colsum)
        c = [colsum.count(i) for i in range(3)]

        if sum(colsum) != upper + lower or min(lower, upper) < c[2] or max(lower, upper) > n:
            return []
        ans = [[], []]
        upper -= c[2]
        for i in range(n):
            if colsum[i] == 0:
                ans[0].append(0)
                ans[1].append(0)
            elif colsum[i] == 2:
                ans[0].append(1)
                ans[1].append(1)
            else:
                if upper > 0:
                    ans[0].append(1)
                    ans[1].append(0)
                    upper -= 1
                else:
                    ans[0].append(0)
                    ans[1].append(1)
        return ans

    def closedIsland(self, grid: List[List[int]]) -> int:
        import queue
        m = len(grid)
        n = len(grid[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def go(sx, sy, target):
            q = queue.Queue()
            q.put_nowait((sx, sy))
            while not q.empty():
                dx, dy = q.get_nowait()
                grid[dx][dy] = target
                for d in dirs:
                    px = dx + d[0]
                    py = dy + d[1]
                    if 0 <= px < m and 0 <= py < n and grid[px][py] == 0:
                        q.put_nowait((px, py))

        for i in [0, m - 1]:
            for j in range(n):
                if grid[i][j] == 0:
                    go(i, j, -1)
        for i in range(1, m - 1):
            for j in [0, n - 1]:
                if grid[i][j] == 0:
                    go(i, j, -1)
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ans += 1
                    go(i, j, ans + 1)
        return ans

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lt = [0] * 26
        for l in letters:
            lt[ord(l) - ord('a')] += 1
        wt = []
        for w in words:
            t = [0] * 26
            for l in w:
                t[ord(l) - ord('a')] += 1
            flag = True
            total = 0
            for i in range(26):
                total += t[i] * score[i]
                if t[i] > lt[i]:
                    flag = False
            if flag:
                t.append(total)
                wt.append(t)
        rs = [w[-1] for w in wt]
        for i in range(len(rs) - 1)[::-1]:
            rs[i] += rs[i + 1]

        n = len(wt)
        best = [0]

        def dfs(deep, total_v, bag):
            if deep == n:
                best[0] = max(total_v, best[0])
                return
            if total_v + rs[deep] <= best[0]:
                return
            dfs(deep + 1, total_v, bag.copy())  # 不拿
            for i in range(26):
                bag[i] -= wt[deep][i]
                if bag[i] < 0:
                    return
            dfs(deep+1, total_v + wt[deep][-1], bag.copy())

        dfs(0, 0, lt)
        return best[0]


if __name__ == '__main__':
    s = Solution()
    # print(s.reconstructMatrix(upper=5, lower=5, colsum=[2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))
    # print(s.reconstructMatrix(upper=9, lower=2, colsum=[0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2]))
    # print(s.closedIsland([[1,1,1],[1,0,1],[0,1,0]]))
    # print(s.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    print(s.maxScoreWords(["add", "dda", "bb", "ba", "add"],
                          ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c", "c", "d", "d", "d"],
                          [3, 9, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
