from typing import *
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            r = numBottles % numExchange
            ans+=numBottles-r
            numBottles = (numBottles // numExchange) + r
        ans += numBottles
        return ans

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        from collections import Counter
        edgemap = [[] for _ in range(n)]
        for e in edges:
            edgemap[e[0]].append(e[1])
            edgemap[e[1]].append(e[0])
        c = Counter()
        ans = [0] * n

        def dfs(i,cnter):

            ans[i] = 1
            for child in edgemap[i]:
                if ans[child] == 0:
                    ct = Counter()
                    dfs(child,ct)
                    ans[i]+=ct[labels[i]]
                    cnter.update(ct)

            cnter[labels[i]] += 1

        dfs(0,c)
        return ans


    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        # lastindex = {}
        previndex = [-1]*n
        firstindex = {}
        for i in range(n):
            # if s[i] in lastindex:
            #     previndex[i] = lastindex[s[i]]
            # lastindex[s[i]] = i
            if s[i] not in firstindex:
                firstindex[s[i]] = i
            else:
                previndex[i] = firstindex[s[i]]

        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            if previndex[i] == -1:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = dp[previndex[i]]

        return dp[-1]




    def func(self, arr,l,r):
        if r< l:
            return -1000000000
        ans = arr[l]
        for i in range(l+1,r+1):
            ans &= arr[i]
        return ans

    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l,r = 0, 0
        ans = 10**9

        ftable = [[-1000000000]*n for _ in range(n)]
        for i in range(n):
            ftable[i][i] = arr[i]

        for i in range(n):
            for j in range(i+1,n):
                ftable[i][j] = ftable[i][j-1] & arr[j]

        # while l <= r and r < n:
        #     # v = self.func(arr,l,r)
        #     v = ftable[l][r]
        #     ans = min(ans,abs(v-target))
        #     if v > target:
        #         r+=1
        #     elif v == target:
        #         return 0
        #     else:
        #         l+=1
        #         r=l

        return ans

if __name__ == '__main__':
    s = Solution()
    # print(s.numWaterBottles(15,4))
    # print(s.numWaterBottles(9,3))
#     print(s.countSubTrees(7,
# [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
# "abaedcd"))
#     print(s.countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))
#     print(s.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))
#     print(s.countSubTrees(n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"))
#     print(s.countSubTrees(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"))
#     print(s.countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"))

    print(s.maxNumOfSubstrings(s = "adefaddaccc"))
    print(s.maxNumOfSubstrings(s = "abbaccd"))
    # print(s.maxNumOfSubstrings())
    # print(s.maxNumOfSubstrings())


    # print(s.closestToTarget(arr = [9,12,3,7,15], target = 5))
    # print(s.closestToTarget(arr = [1000000,1000000,1000000], target = 1))
    # print(s.closestToTarget(arr = [1,2,4,8,16], target = 0))
    # print(s.closestToTarget([5,89,79,44,45,79], 965))
