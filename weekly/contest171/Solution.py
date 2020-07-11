from typing import *
import time


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n - 1
        while True:
            sb = str(b)
            if sb.count('0') == 0:
                return [a, b]
            idx = sb[::-1].index('0')
            for i in range(idx + 1):
                a += 10 ** i
            b = n - a
        return None

    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        mx = max(max(len(a), len(b)), len(c))
        a = '0' * (mx - len(a)) + a
        b = '0' * (mx - len(b)) + b
        c = '0' * (mx - len(c)) + c
        ans = 0
        for i in range(mx):
            ai = int(a[i])
            bi = int(b[i])
            ci = int(c[i])
            if ai | bi != ci:
                if ci == 1:
                    ans += 1
                else:
                    ans += ai + bi
        return ans

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        csm = set()
        if len(connections) < n - 1:
            return -1
        for c in connections:
            if c[0] in csm and c[1] in csm:
                continue

            csm.add(c[0])
            csm.add(c[1])
        return n - len(csm)
        # csm = []
        # if len(connections) < n - 1:
        #     return -1
        # for c in connections:
        #     id0 = -1
        #     id1 = -1
        #     for i,cs in enumerate(csm):
        #         if c[0] in cs:
        #             id0 = i
        #         if c[1] in cs:
        #             id1 = i
        #     if id0 == id1:
        #         if id0  == -1:
        #             csm.append(set(c))
        #         else:
        #             continue
        #     elif id0 == -1:
        #         csm[id1].add(c[0])
        #     elif id1 == -1:
        #         csm[id0].add(c[1])
        #     else:
        #         csm[id0] = csm[id0] | csm[id1]
        #         csm[id0].add(c[0])
        #         csm[id0].add(c[1])
        #         csm.remove(csm[id1])
        # total = sum(list(map(len,csm)))
        # return n - total + len(csm) - 1

    def minimumDistance(self, word: str) -> int:
        n = len(word)
        word_map = {'A': (0, 0),'B': (0, 1),'C': (0, 2),
                    'D': (0, 3),'E': (0, 4),'F': (0, 5),
                    'G': (1, 0),'H': (1, 1),'I': (1, 2),
                    'J': (1, 3),'K': (1, 4),'L': (1, 5),
                    'M': (2, 0),'N': (2, 1),'O': (2, 2),
                    'P': (2, 3),'Q': (2, 4),'R': (2, 5),
                    'S': (3, 0),'T': (3, 1),'U': (3, 2),
                    'V': (3, 3),'W': (3, 4), 'X': (3, 5),
                    'Y': (4, 0),'Z': (4, 1)}
        prev = [[0, word_map[word[0]], None]]

        maxdist = [0]*n
        for i in range(n-1)[::-1]:
            wi = word_map[word[i]]
            wip1 = word_map[word[i+1]]
            d = abs(wi[0] - wip1[0]) + abs(wi[1] - wip1[1])
            maxdist[i] = maxdist[i+1]+d

        for i in range(1, n):
            nw = word_map[word[i]]
            temp = []
            for sp in prev:
                for lr in range(2):
                    if sp[lr+1] is None:
                        d = 0
                    else:
                        d = abs(nw[0] - sp[lr+1][0]) + abs(nw[1] - sp[lr+1][1])
                    s = sp.copy()
                    s[0] += d
                    s[lr+1] = nw
                    temp.append(s)
            mv = min(list(map(lambda x: x[0], temp)))
            prev = [p for p in temp if p[0] <= mv + maxdist[i-1]]
        return min(list(map(lambda x:x[0],prev)))


if __name__ == '__main__':
    s = Solution()
    # print(s.getNoZeroIntegers(1057))
    # print(s.getNoZeroIntegers(1010))
    # print(s.getNoZeroIntegers(100000001000000))
    # print(s.getNoZeroIntegers(10506600))
    print(s.minimumDistance('CAKE'))
    print(s.minimumDistance('HAPPY'))
    print(s.minimumDistance('NEW'))
    print(s.minimumDistance('YEAR'))
    print(s.minimumDistance('SHH'))
    # print(s.makeConnected(100,
    #                       [[17, 51], [33, 83], [53, 62], [25, 34], [35, 90], [29, 41], [14, 53], [40, 84], [41, 64],
    #                        [13, 68], [44, 85], [57, 58], [50, 74], [20, 69], [15, 62], [25, 88], [4, 56], [37, 39],
    #                        [30, 62], [69, 79], [33, 85], [24, 83], [35, 77], [2, 73], [6, 28], [46, 98], [11, 82],
    #                        [29, 72], [67, 71], [12, 49], [42, 56], [56, 65], [40, 70], [24, 64], [29, 51], [20, 27],
    #                        [45, 88], [58, 92], [60, 99], [33, 46], [19, 69], [33, 89], [54, 82], [16, 50], [35, 73],
    #                        [19, 45], [19, 72], [1, 79], [27, 80], [22, 41], [52, 61], [50, 85], [27, 45], [4, 84],
    #                        [11, 96], [0, 99], [29, 94], [9, 19], [66, 99], [20, 39], [16, 85], [12, 27], [16, 67],
    #                        [61, 80], [67, 83], [16, 17], [24, 27], [16, 25], [41, 79], [51, 95], [46, 47], [27, 51],
    #                        [31, 44], [0, 69], [61, 63], [33, 95], [17, 88], [70, 87], [40, 42], [21, 42], [67, 77],
    #                        [33, 65], [3, 25], [39, 83], [34, 40], [15, 79], [30, 90], [58, 95], [45, 56], [37, 48],
    #                        [24, 91], [31, 93], [83, 90], [17, 86], [61, 65], [15, 48], [34, 56], [12, 26], [39, 98],
    #                        [1, 48], [21, 76], [72, 96], [30, 69], [46, 80], [6, 29], [29, 81], [22, 77], [85, 90],
    #                        [79, 83], [6, 26], [33, 57], [3, 65], [63, 84], [77, 94], [26, 90], [64, 77], [0, 3],
    #                        [27, 97], [66, 89], [18, 77], [27, 43]]))
