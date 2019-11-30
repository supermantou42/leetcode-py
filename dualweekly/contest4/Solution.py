from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def get_pub(arr1: List[int], arr2: List[int]):
            i = 0
            j = 0
            ans = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] == arr2[j]:
                    ans.append(arr2[j])
                    i += 1
                    j += 1
                elif arr1[i] < arr2[j]:
                    i += 1
                else:
                    j += 1
            return ans
        ans = get_pub(arr1,arr2)
        ans = get_pub(ans, arr3)
        return ans

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        def find_bnd(root: TreeNode, nowval):
            if root is None:
                return nowval,nowval
            else:
                lmax, lmin = find_bnd(root.left, root.val)
                rmax, rmin = find_bnd(root.right, root.val)
                return max(lmax,rmax), min(lmin,rmin)
        max_, min_ = find_bnd(root2,root2.val)

        list1 = []

        def mid(root: TreeNode):
            if root is None:
                return
            mid(root.left)
            list1.append(root.val)
            mid(root.right)

        mid(root1)


        def go(root: TreeNode, tar):
            if root is None:
                return False
            if root.val == tar:
                return True
            elif root.val < tar:
                return go(root.right,tar)
            else:
                return go(root.left,tar)

        for i in list1:
            t = target - i
            if min_ <= t <= max_:
                if go(root2,t):
                    return True
        return False

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        def go(num):
            s = list(str(num))[::-1]
            for i in range(len(s))[:-1]:
                if abs(int(s[i]) - int(s[i+1])) != 1:

                    return -1
            for i in range(len(s))[:-1]:
                if int(s[i]) < int(s[i+1]):
                    if int(s[i]) < 8:
                        s[i] = str(int(s[i]) + 2)
                        st = int(s[i]) - 1
                        for j in range(i-1,-1,-1):
                            if st >= 0:
                                s[j] = str(st)
                                st -= 1
                            else:
                                s[j] = '1'
                                st = 0
                        return int(''.join(s[::-1]))

            if s[-1] == '9':
                ll = len(s) + 1
                s = '10' * (ll // 2)
                if ll % 2 == 1:
                    s += '1'
                return int(s)
            st = int(s[-1]) + 1
            ll = len(s)
            ss = ''
            for i in range(ll):
                if st >= 0:
                    ss += str(st)
                    st -= 1
                else:
                    ss += '1'
                    st = 0
            return int(ss)

        ans = []
        st = low
        if go(low) < 0:
            ss = str(low)
            ll = len(ss)
            st = '10' * (ll // 2)
            if ll % 2 == 1:
                st += '1'
            st = int(st)
        while st <= high:
            a = go(st)
            # if a < 0:
            #     a += 1
            if st >= low:
                ans.append(st)
            st = a
        return ans

if __name__ == '__main__':
    s = Solution()
    # print(s.twoSumBSTs(root1,root2,5))
    # print(s.countSteppingNumbers(low =789, high = 1234))
    print(s.countSteppingNumbers(low =1713834549,high=1800528026))