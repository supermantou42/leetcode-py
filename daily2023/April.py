from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans_ = [0] * n
        path_map = [[] for _ in range(n)]
        for x,y in paths:
            if x > y:
                x,y = y, x
            path_map[y-1].append(x-1)
        ans_[0] = 1
        for idx in range(1, n):
            hit = []
            for before_dots in path_map[idx]:
                hit.append(ans_[before_dots])
            for i in range(4):
                if i+1 not in hit:
                    ans_[idx]=i+1
                    break

        return ans_



if __name__ == '__main__':
    s = Solution()
    print(s.gardenNoAdj(3,  [[1,2],[2,3],[3,1]]))
    print(s.gardenNoAdj(4,  [[1,2],[3,4]]))
    print(s.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))