from typing import *
import time

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(0,n,2):
            ans += [nums[i+1]] * nums[i]
        return ans

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        ddate = [[0] * n for _ in range(m)]
        ans = [[0] * n for _ in range(m)]
        ddate[0][0] = mat[0][0]
        for i in range(1,m):
            ddate[i][0] = ddate[i-1][0] + mat[i][0]
        for j in range(1,n):
            ddate[0][j] = ddate[0][j-1] + mat[0][j]
        for i in range(1,m):
            for j in range(1,n):
                ddate[i][j] = ddate[i-1][j] + ddate[i][j-1] - ddate[i-1][j-1] + mat[i][j]


        for i in range(m):
            for j in range(n):
                sx = i - K
                sy = j - K
                ex = i + K
                ey = j + K
                sx = sx if sx >= 0 else 0
                sy = sy if sy >= 0 else 0
                ex = ex if ex < m else m-1
                ey = ey if ey < n else n-1

                l = ddate[ex][sy-1] if sy > 0 else 0
                t = ddate[sx-1][ey] if sx > 0 else 0
                lt = ddate[sx-1][sy-1] if sx>0 and sy > 0 else 0

                ans[i][j] = ddate[ex][ey] - l - t +lt
        return ans

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = [0]
        def dfs(node:TreeNode, state:list):
            if node is None:
                return
            if state[0] == 0:
                total[0] += node.val
            next_state = [state[1], node.val % 2]
            dfs(node.left, next_state)
            dfs(node.right, next_state)
        dfs(root,[1,1])
        return total[0]

    def distinctEchoSubstrings(self, text: str) -> int:
        orda = ord('a')
        val = list(map(lambda x:ord(x)-orda,text))
        n = len(text)
        ans = set()
        for window_size in range(1, n//2 + 1):
            temp = [-1] * n
            bias = 26 ** (window_size-1)
            value = 0
            if window_size == 1:
                temp = val.copy()
                for i in range(n-1):
                    if temp[i] == temp[i+1]:
                        ans.add((1,temp[i]))
                if len(set(temp)) == len(temp):
                    break
            else:
                for i in range(window_size):
                    value = value * 26 + val[i]
                temp[window_size-1] = value
                for i in range(window_size,n):
                    value = (value - val[i-window_size] * bias)* 26 + val[i]
                    temp[i] = value
                for i in range(window_size-1,n-window_size):
                    if temp[i] == temp[i+window_size]:
                        ans.add((window_size,temp[i]))
                if len(set(temp)) - 1 == len(temp) - window_size + 1:
                    break
        return len(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.distinctEchoSubstrings('abcabcabc'))
    print(s.distinctEchoSubstrings('leetcodeleetcode'))