from typing import *
import time


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortString(self, s: str) -> str:
        import collections
        n = len(s)
        c = collections.Counter(s)
        keys = list(c.keys())
        keys.sort()
        result = ''
        reverse = False
        while n > 0:
            if reverse:
                for k in keys[::-1]:
                    if c[k] > 0:
                        result += k
                        c[k] -= 1
                        n -= 1
                reverse = False
            else:
                for k in keys:
                    if c[k] > 0:
                        result += k
                        c[k] -= 1
                        n -= 1
                reverse = True
        return result

    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        table = [[0] * 5 for _ in range(n)]
        idmap = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        if s[0] in idmap:
            if n == 1:
                return 0
            table[0][idmap[s[0]]] += 1

        minret = 1
        for i in range(1, n):
            table[i] = table[i - 1].copy()
            if s[i] in idmap:
                table[i][idmap[s[i]]] ^= 1
            if sum(table[i]) == 0:
                minret = i + 1
        for m in range(minret + 1, n + 1)[::-1]:
            outflag = False
            for i in range(m, n):
                flag = True
                for j in range(5):
                    if table[i][j] - table[i - m][j] != 0:
                        flag = False
                        break
                if flag:
                    outflag = True
                    break
            if outflag:
                return m
        return minret

    def longestZigZag(self, root: TreeNode) -> int:
        ret = [0]
        def dfs(node:TreeNode):
            if node is None:
                return 0,0
            _, r = dfs(node.left)
            l, _ = dfs(node.right)
            ret[0] = max([ret[0],l+1,r+1])
            return r+1,l+1
        dfs(root)
        return ret[0]

    def maxSumBST(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node:TreeNode):
            if node is None:
                return True,0
            leftib,leftv = dfs(node.left)
            rightib,rightv = dfs(node.right)
            if leftib and rightib:
                isbst = True
                if node.left is not None and node.left.val >= node.val:
                    isbst = False
                if isbst and node.right is not None and node.right.val <= node.val:
                    isbst = False
                if isbst:
                    nodev = node.val + leftv + rightv
                    res[0] = max(res[0],nodev)
                    return True,nodev
                else:
                    return False,0
            else:
                return False,0
        dfs(root)
        return res[0]

if __name__ == '__main__':
    s = Solution()