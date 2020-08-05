from typing import *

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high-low+1)//2
        if low % 2==1 and (high-low+1) %2 == 1:
            n+=1
        return n

    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(2)]
        if arr[0] % 2 == 1:
            dp[1][0] = 1
        else:
            dp[0][0] = 1

        for i in range(1,n):
            if arr[i] % 2 == 0:
                dp[0][i] = dp[0][i-1] + 1
                dp[1][i] = dp[1][i-1]
            else:
                dp[0][i] = dp[1][i-1]
                dp[1][i] = dp[0][i-1] + 1

        return sum(dp[1]) % (10**9+7)

    def numSplits(self, s: str) -> int:
        n = len(s)
        a = [0]*n
        b = [0]*n
        set1 = set()
        for i in range(n):
            set1.add(s[i])
            a[i] = len(set1)
        set1.clear()
        for i in range(n)[::-1]:
            set1.add(s[i])
            b[i] = len(set1)
        cnt = 0
        for i in range(n-1):
            if a[i] == b[i+1]:
                cnt+=1
        return cnt

    def minNumberOperations(self, target: List[int]) -> int:
        # ans = 0
        # n = len(target)
        # while max(target) > 0:
        #     idx = target.index(max(target))
        #     prev = target[idx]
        #     ans += prev
        #     for i in range(idx+1,n):
        #         prev = min(prev,target[i])
        #         if prev == 0:
        #             break
        #         target[i] -= prev
        #     prev = target[idx]
        #     for i in range(idx)[::-1]:
        #         prev = min(prev,target[i])
        #         if prev == 0:
        #             break
        #         target[i] -= prev
        #     target[idx] = 0
        # return ans

        n = len(target)
        ans = target[0]
        for i in range(1,n):
            if target[i] > target[i-1]:
                ans += target[i] - target[i-1]
        return ans

if __name__ == '__main__':
    s = Solution()
    # print(s.numOfSubarrays([1,3,5]))
    # print(s.numOfSubarrays([2,4,6]))
    # print(s.numOfSubarrays([1,2,3,4,5,6,7]))
    # print(s.numOfSubarrays([100,100,99,99]))
    # print(s.numOfSubarrays([7]))
    # print(s.numSplits("aacaba"))
    # print(s.numSplits(s = "abcd"))
    # print(s.numSplits(s = "aaaaa"))
    # print(s.numSplits(s = "acbadbaada"))
    print(s.minNumberOperations([1,2,3,2,1]))
    print(s.minNumberOperations( [3,1,1,2]))
    print(s.minNumberOperations([3,1,5,4,2]))
    print(s.minNumberOperations([1,1,1,1]))