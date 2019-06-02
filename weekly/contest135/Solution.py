from typing import *
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        # (x-x1)(y2-y1)==(y-y1)(x2-x1)
        dy = points[1][1] - points[0][1]
        dx = points[1][0] - points[0][0]
        if ((points[2][0] - points[0][0]) * dy) == ((points[2][1] - points[0][1]) * dx):
            return False
        return True

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def go(root: TreeNode, ans) -> int:
            if root.right is not None:
                ans = go(root.right, ans)
            ans += root.val
            root.val = ans
            if root.left is not None:
                ans = go(root.left, ans)
            return ans

        go(root, 0)
        return root

    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        cost = [[999] * n for _ in range(n)]
        prepare_list = []
        for i in range(n):
            for j in range(2, n - 1):
                cost[i][(i + j) % n] = A[i] * A[(i + j) % n]
                prepare_list.append((i, (i + j) % n))
        prepare_list.sort(key=lambda x: cost[x[0]][x[1]])
        ans = []
        # for t in prepare_list:
        #

    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        maxmove = 0
        minimove = 0
        n = len(stones)
        # mini
        stone_tmp = stones.copy()
        while True:
            diff = [stone_tmp[i] - stone_tmp[i - 1] for i in range(1, n)]
            if diff.count(0) == n:
                break
            max_value = 0
            max_index = 0
            if diff[0] > diff[-1]:
                for i in range(1, n - 1):
                    if diff[i] > max_value:
                        max_value = diff[i]
                        max_index = i
                for i in range(max_index):
                    stone_tmp[i] = stone_tmp[i+1]
                stone_tmp[max_index+1] = (stone_tmp[max_index]+stone_tmp[max_index+1])//2
            else:
                for i in range(0, n - 2):
                    if diff[i] > max_value:
                        max_value = diff[i]
                        max_index = i
                for i in range(n-1,max_index,-1):
                    stone_tmp[i] = stone_tmp[i-1]
                stone_tmp[max_index] = (stone_tmp[max_index]+stone_tmp[max_index+1])//2

            minimove += 1

if __name__ == '__main__':
    s = Solution()
    print(s.isBoomerang([[1, 1], [2, 2], [3, 3]]))
