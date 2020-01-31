from typing import *
import time


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        import collections
        d = collections.Counter([l for l, r in zip(s1, s2) if l != r])
        dx = d['x']
        dy = d['y']
        if (dx + dy) % 2 == 1 or len(s1) != len(s2):
            return -1
        return sum(divmod(dx, 2) + divmod(dy, 2))

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [n % 2 for n in nums]
        n = len(nums)
        accu = nums.copy()
        for i in range(1,n):
            accu[i] += accu[i-1]
        if accu[-1] < k:
            return 0
        from collections import Counter
        c = Counter(accu)
        ans = 0
        c[0] += 1
        for i in c.keys():
            ans += c[i+k] * c[i]
        return ans

    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        ans = ''
        lbc = 0
        for i in range(n):
            if s[i] == '(':
                lbc += 1
                ans += s[i]
            elif s[i] == ')':
                if lbc > 0:
                    ans += s[i]
                    lbc -= 1
            else:
                ans += s[i]
        if lbc > 0:
            temp = ''
            for a in ans[::-1]:
                if a != '(':
                    temp += a
                elif lbc > 0:
                    lbc -= 1
                else:
                    temp += a
            ans = temp[::-1]

        return ans

    def isGoodArray(self, nums: List[int]) -> bool:
        # def gcd(a,b):
        #     while True:
        #         x,y = divmod(b,a)
        #         if y == 0:
        #             return a
        #         b = a
        #         a = y
        import math
        a = nums[0]
        for n in nums[1:]:
            a = math.gcd(a,n)
        return a == 1

if __name__ == '__main__':
    s = Solution()
    # print(s.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
    # print(s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
    # print(s.minRemoveToMakeValid('lee(t(c)o)de)'))
    # print(s.minRemoveToMakeValid("a)b(c)d"))
    # print(s.minRemoveToMakeValid("))(("))
    # print(s.minRemoveToMakeValid("(a(b(c)d)"))
    print(s.isGoodArray([29,6,10]))