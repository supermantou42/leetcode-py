from typing import *


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        i = 0
        for c in s:
            if c == 'L':
                i += 1
            else:
                i -= 1
            if i == 0:
                cnt += 1
        return cnt

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        qipan = [[0 for _ in range(8)] for _ in range(8)]
        for q in queens:
            qipan[q[0]][q[1]] = 1
        dir = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1),
        ]
        ans = []
        for d in dir:
            ckp = king.copy()
            while True:
                ckp[0] += d[0]
                ckp[1] += d[1]
                if ckp[0] < 0 or ckp[0] > 7 or ckp[1] < 0 or ckp[1] > 7:
                    break

                if qipan[ckp[0]][ckp[1]] == 1:
                    ans.append(ckp.copy())
                    break

        return ans

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        a = 6 ** n

        def one(r):
            return int(((n - r) * 5 + 6) * (6 ** (n - r - 1)))
        for r in rollMax:
            a -= one(r+1)


        return a % int(10**9 + 7)


if __name__ == '__main__':
    s = Solution()
    import time

    st = time.time()
    print(s.dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]))
    print(s.dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]))
    print(time.time() - st)
