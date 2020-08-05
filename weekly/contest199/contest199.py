from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = [None] * len(indices)
        for i in range(len(indices)):
            ss[indices[i]] = s[i]
        return ''.join(ss)

    def minFlips(self, target: str) -> int:
        prev = target[-1]
        cnt = 0
        for t in target[-2::-1]:
            if t != prev:
                cnt+=1
                prev=t
        if target[0] == '1':
            cnt+=1
        return cnt

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(node:TreeNode):
            if node is None:
                return [0]*distance
            if node.left is None and node.right is None:
                return [1] + [0]*(distance-1)

            l = dfs(node.left)
            r = dfs(node.right)
            for i in range(distance):
                for j in range(distance-i-1):
                    self.ans += l[i]*r[j]
            return [0] + [l[i]+r[i] for i in range(distance-1)]
        dfs(root)
        return self.ans
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        n = len(s)
        if n <= 1:
            return n
        if n <= k:
            return 0
        comp = []
        prev_cnt = 1
        for i in range(1,n):
            if s[i] == s[i-1]:
                prev_cnt += 1
            else:
                comp.append([s[i-1], prev_cnt])
                prev_cnt=1
        if prev_cnt > 0:
            comp.append([s[-1], prev_cnt])
        m = len(comp)
        dp = [[0]*m for _ in range(k+1)]
        for i in range(m):
            if comp[i][1] == 1:
                dp[0][i] = 1
            elif 2<=comp[i][1] < 10:
                dp[0][i] = 2
            elif 10<=comp[i][1] < 100:
                dp[0][i] = 3
            else:
                dp[0][i] = 4
        for i in range(1,k+1):
            for j in range(m):








if __name__ == '__main__':

    s = Solution()
    # print(s.restoreString(s = "", indices = []))
    # print(s.minFlips(target = "10111"))
    # print(s.minFlips(target = "101"))
    # print(s.minFlips(target = "00000"))
    # print(s.minFlips(target = "001011101"))
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    #
    # print(s.countPairs(root,3))
    # print(s.getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
    print(s.getLengthOfOptimalCompression(s = "aabbaa", k = 2))
    # print(s.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0))