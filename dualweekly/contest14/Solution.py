from typing import *


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        return True


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution:
    def toHexspeak(self, num: str) -> str:
        num = hex(int(num))[2:].upper()
        num = num.replace('1', 'I')
        num = num.replace('0', 'O')
        accept = {"A", "B", "C", "D", "E", "F", "I", "O"}
        for n in num:
            if n not in accept:
                return 'ERROR'
        return num

    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for itv in intervals:
            if itv[1] <= toBeRemoved[0] or itv[0] >= toBeRemoved[1]:
                ans.append(itv)
            elif itv[0] < toBeRemoved[0] < itv[1] < toBeRemoved[1]:
                ans.append([itv[0], toBeRemoved[0]])
            elif itv[0] >= toBeRemoved[0] and itv[1] <= toBeRemoved[1]:
                pass
            elif toBeRemoved[0] < itv[0] < toBeRemoved[1] < itv[1]:
                ans.append([toBeRemoved[1], itv[1]])
            else:
                if itv[0] != toBeRemoved[0]:
                    ans.append([itv[0], toBeRemoved[0]])
                if toBeRemoved[1] != itv[1]:
                    ans.append([toBeRemoved[1], itv[1]])
        return ans

    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        child = [[] for _ in range(nodes)]
        root = parent.index(-1)
        for i in range(nodes):
            if parent[i] >= 0:
                child[parent[i]].append(i)

        def go(now):
            if len(child[now]) == 0:
                if value[now] == 0:
                    return 0, 0
                return value[now], 1
            total = value[now]
            cnt = 1
            for ch in child[now]:
                t, c = go(ch)
                total += t
                cnt += c
            if total == 0:
                return 0, 0
            return total, cnt

        t, c = go(root)
        if t == 0:
            return 0
        else:
            return c

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def go(tr: 'Point', bl: 'Point'):
            dx = tr.x - bl.x
            dy = tr.y - bl.y
            if dx == 0 and dy == 0:
                return 1  # if sea.hasShips(tr, bl) else 0
            if dx >= dy:
                mx = (tr.x + bl.x) // 2
                bl1 = bl
                tr1 = Point(mx, tr.y)
                bl2 = Point(mx + 1, bl.y)
                tr2 = tr
            else:
                my = (tr.y + bl.y) // 2
                bl1 = Point(bl.x, my + 1)
                tr1 = tr
                bl2 = bl
                tr2 = Point(tr.x, my)

            total = 0
            if sea.hasShips(tr1, bl1):
                total += go(tr1, bl1)
            if sea.hasShips(tr2, bl2):
                total += go(tr2, bl2)
            return total

        return go(topRight, bottomLeft)


if __name__ == '__main__':
    s = Solution()
    # print(s.toHexspeak('3'))
    print(s.countShips(Sea(), Point(2, 2), Point(0, 0)))
