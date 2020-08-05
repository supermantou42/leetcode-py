from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        nowmin = prices[0]
        for i in range(n):
            nowmin = min(nowmin, prices[i])
            prices[i] -= nowmin
        return max(prices)

    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))

    def add(self, a: int, b: int) -> int:
        '''
         python整数无限长，负数需要截断特殊处理
        '''
        x = 0xffffffff
        a, b = a & x, b & x
        while b:
            c = a ^ b
            d = (a & b) << 1 & x
            a = c
            b = d
        return a if a <= 0x7fffffff else ~(a ^ x)

    def constructArr(self, a: List[int]) -> List[int]:
        b = a.copy()
        c = a.copy()
        n = len(a)
        for i in range(1, n):
            b[i] *= b[i - 1]
            c[n - 1 - i] *= c[n - i]
        return [c[1]] + [b[i - 1] * c[i + 1] for i in range(1, n - 1)] + [b[-2]]

    def strToInt(self, str: str) -> int:
        negative_flag = False
        ans = 0
        str = str.strip()
        n = len(str)
        if n == 0:
            return 0
        if str[0] == '-':
            negative_flag = True
            str = str[1:]
            n -= 1
        for i in range(n):
            if '0' <= str[i] <= '9':
                ans = ans * 10 + ord(str[i]) - ord('0')
            else:
                return 0
        if negative_flag:
            if ans >= 2147483648:
                return -2147483648
            return -ans
        elif ans >= 2147483647:
            return 2147483647
        else:
            return ans

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if p.val > q.val:
            tmp = p
            p = q
            q= tmp
        if p.val < root.val < q.val:
            return root
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return self.lowestCommonAncestor(root.right,p,q)

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None
        def dfs(node:TreeNode,p,q):
            if node is None:
                return 0
            if self.ans is not None:
                return 0
            ret = dfs(node.left,p,q) + dfs(node.right,p,q)
            if ret == 2:
                self.ans = node
                return 0
            if p == node or q == node:
                if ret == 0:
                    return 1
                self.ans = node
                return 0
            return ret
        dfs(root,p,q)
        return self.ans

