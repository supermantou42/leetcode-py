from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 32-Ⅰ
    def levelOrder1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = [root]
        nextqueue = []
        ans = []
        while queue:
            nextqueue = []
            for q in queue:
                ans.append(q.val)
                if q.left is not None:
                    nextqueue.append(q.left)
                if q.right is not None:
                    nextqueue.append(q.right)

            queue = nextqueue
        return ans

    # 32-Ⅱ
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:

        # BFS
        # if root is None:
        #     return []
        # queue = [root]
        # nextqueue = []
        # ans = []
        # while queue:
        #     temp = []
        #     nextqueue = []
        #     for q in queue:
        #         temp.append(q.val)
        #         if q.left is not None:
        #             nextqueue.append(q.left)
        #         if q.right is not None:
        #             nextqueue.append(q.right)
        #     ans.append(temp)
        #     queue = nextqueue
        # return ans
        # DFS
        if root is None:
            return []
        ans = []
        def go(node,depth):
            if node is None:
                return
            if len(ans)== depth:
                ans.append([])
            ans[depth].append(node.val)
            go(node.left,depth+1)
            go(node.right,depth+1)
        go(root,0)
        return ans

    # 32-Ⅲ
    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        def go(node,depth):
            if node is None:
                return
            if len(ans)== depth:
                ans.append([])
            ans[depth].append(node.val)
            go(node.left,depth+1)
            go(node.right,depth+1)
        go(root,0)
        for i in range(1,len(ans),2):
            ans[i] = ans[i][::-1]

        return ans
