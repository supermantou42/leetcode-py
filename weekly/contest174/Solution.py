from typing import *
import time
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = list(map(sum,mat))
        mat = [[i,mat[i]] for i in range(len(mat))]
        mat.sort(key=lambda x:(x[1],x[0]))
        return list(map(lambda x:x[0],mat))[:k]

    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        n = len(arr)
        c = Counter(arr)
        a = [v for _,v in c.items()]
        a.sort(reverse=True)
        cnt = 0
        for i in range(len(a)):
            cnt += a[i]
            if cnt >= n // 2:
                return i + 1

    def maxProduct(self, root: TreeNode) -> int:
        total_val = []
        def postsearch(node: TreeNode):
            if node is None:
                return 0
            l = postsearch(node.left)
            r = postsearch(node.right)
            node.val += l + r
            total_val.append(node.val)
            return node.val

        n = postsearch(root)
        total_val = [(abs(v - (n / 2)),v) for v in total_val]
        ansv = min(total_val,key=lambda x:x[0])
        return (n-ansv[1]) * ansv[1] % (10**9+7)

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if n == 1:
            return 1

        calidx = list(range(n))
        calidx.sort(key=lambda x:arr[x])
        table = [0]*n
        for idx in calidx:
            res = 0
            l = max(idx - d,0)
            r = min(idx + d + 1, n)
            idv = arr[idx]
            for i in range(l,idx)[::-1]:
                if arr[i] < idv:
                    res = max(res,table[i])
                else:
                    break

            for i in range(idx+1,r):
                if arr[i] < idv:
                    res = max(res,table[i])
                else:
                    break
            table[idx] = res + 1

        return max(table)



if __name__ == '__main__':
    s = Solution()
    print(s.maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2))
    print(s.maxJumps(arr = [3,3,3,3,3], d = 3))
    print(s.maxJumps(arr = [7,6,5,4,3,2,1], d = 1))
    print(s.maxJumps(arr = [7,1,7,1,7,1], d = 2))
    print(s.maxJumps(arr = [66], d = 1))
    print(s.maxJumps([83,11,83,70,75,45,96,11,80,75,67,83,6,51,71,64,64,42,70,23,11,24,95,65,1,54,31,50,18,16,11,86,2,48,37,34,65,67,4,17,33,70,16,73,57,96,30,26,56,1,16,74,82,77,82,62,32,90,94,33,58,23,23,65,70,12,85,27,38,100,93,49,96,96,77,37,69,71,62,34,4,14,25,37,70,3,67,88,20,30],29))