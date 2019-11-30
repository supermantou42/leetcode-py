from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        changes = [0] * (n + 1)
        for book in bookings:
            changes[book[0] - 1] += book[2]
            changes[book[1]] -= book[2]
        num = 0
        for i in range(n):
            num += changes[i]
            ans[i] = num
        return ans

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        if root.val not in to_delete:
            ans.append(root)
        queue = [root]
        next_queue = []
        while True:
            while len(queue) > 0:
                r = queue.pop(0)
                # if r is None:
                #     continue
                if r.left is not None:
                    next_queue.append(r.left)
                    if r.left.val in to_delete:
                        r.left = None

                if r.right is not None:
                    next_queue.append(r.right)
                    if r.right.val in to_delete:
                        r.right = None

                if r.val in to_delete:
                    if r.left is not None and r.left.val not in to_delete:
                        ans.append(r.left)
                    if r.right is not None and r.right.val not in to_delete:
                        ans.append(r.right)

            if len(next_queue) == 0:
                return ans
            queue = next_queue
            next_queue = []

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        max_deep = 0
        deep = 0
        for s in seq:
            if s == '(':
                deep += 1
                if deep > max_deep:
                    max_deep = deep
            else:
                deep -= 1



if __name__ == '__main__':
    s = Solution()
