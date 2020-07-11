from typing import *
import time


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'

    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        rightmin = [0] * n
        rightmin[-1] = light[-1]
        for i in range(n - 1)[::-1]:
            rightmin[i] = min(rightmin[i + 1], light[i])
        cnt = 1
        lmax = light[0]
        for i in range(n - 1):
            lmax = max(lmax, light[i])
            if lmax + 1 == rightmin[i + 1]:
                cnt += 1
        return cnt

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] > -1:
                sub[manager[i]].append(i)

        def dfs(userid):
            if informTime[userid] == 0:
                return 0
            it = 0
            for s in sub[userid]:
                it = max(it, dfs(s))
            return it + informTime[userid]

        return dfs(headID)

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        tomap = [[] for _ in range(n + 1)]
        for f, to in edges:
            tomap[f].append(to)
            tomap[to].append(f)
        if target == 1:
            if len(tomap[1]) == 0:
                return 1.
            else:
                return 0.
        def dfs(node, visited: set, patn_, deep):
            if node == target:
                return patn_
            if deep < 0:
                return []
            visited.add(node)
            for nn in tomap[node]:
                if nn not in visited:
                    p = dfs(nn, visited, patn_ + [nn], deep - 1)
                    if p:
                        return p
            visited.remove(node)
            return []
        path = dfs(1, set(), [1], t-1)
        if not path:
            return 0.
        if len(tomap[path[-1]]) > 1:
            if len(path) - 1 != t:
                return 0.
        pos = 1.
        for i in range(1, len(path) - 1):
            tomap[path[i]].remove(path[i - 1])
        for p in path[:-1]:
            c = len(tomap[p])
            pos *= 1 / c

        return pos


if __name__ == '__main__':
    s = Solution()
    # print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))
    # print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))
    # print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6))
    # print(s.frogPosition(n=3, edges=[[2, 1], [3, 2]], t=1, target=2))
    # print(s.frogPosition(8,
    #                      [[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]],
    #                      7,
    #                      7))
    print(s.frogPosition(82,
[[2,1],[3,2],[4,2],[5,1],[6,2],[7,2],[8,3],[9,8],[10,6],[11,10],[12,1],[13,1],[14,12],[15,8],[16,3],[17,15],[18,16],[19,17],[20,7],[21,9],[22,9],[23,20],[24,5],[25,10],[26,4],[27,11],[28,8],[29,11],[30,11],[31,7],[32,25],[33,8],[34,27],[35,14],[36,27],[37,9],[38,33],[39,35],[40,6],[41,25],[42,2],[43,25],[44,9],[45,26],[46,23],[47,40],[48,34],[49,26],[50,39],[51,10],[52,47],[53,43],[54,6],[55,49],[56,44],[57,34],[58,15],[59,49],[60,13],[61,32],[62,31],[63,25],[64,50],[65,41],[66,33],[67,2],[68,34],[69,4],[70,49],[71,67],[72,51],[73,19],[74,22],[75,34],[76,13],[77,53],[78,15],[79,62],[80,52],[81,7],[82,63]]
,6,
73))
