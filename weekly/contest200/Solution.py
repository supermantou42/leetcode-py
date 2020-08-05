from typing import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        if n < 3:
            return 0
        # i,j,k = 0,1,2
        # while i < j < k < n:
        cnt = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                if abs(arr[j] - arr[i]) > a:
                    continue
                for k in range(j+1,n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt +=1
        return cnt

    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        a = max(arr[:2])
        prev_cnt = 1
        for i in range(2,n):
            if arr[i] < a:
                prev_cnt+=1
                if prev_cnt == k:
                    return a
            else:
                a = arr[i]
                prev_cnt = 1
        return a

    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt = 0
        for i in range(n-1,0,-1):
            row_cnt = sum(grid[j][i] for j in range(n))
            if row_cnt > n-i:
                return -1
            row_ids = [j for j in range(i) if grid[j][i] == 1]
            st_ids = i
            sc = 0

            for row in row_ids:
                while grid[st_ids][i] == 1:

                    st_ids+=1
                cnt += st_ids-row+sc
                grid.pop(row-sc)
                grid.insert(st_ids-1,[1]*n)
                sc+=1

        return cnt


    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)
        i,j = 0,0
        v = []
        pi,pj = 0,0
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                vv = []
                if pi != i:
                    vv.append(sum(nums1[pi:i]))
                if pj != j:
                    vv.append(sum(nums2[pj:j]))
                if vv:
                    v.append(vv)
                v.append([nums1[i]])
                i+=1
                j+=1
                pi,pj = i,j
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        v.append([sum(nums1[pi:]), sum(nums2[pj:])])
        ans = 0
        for i in range(len(v)):
            ans+=max(v[i])

        return ans

        # dp = [[[0,0] for _ in range(n+1)]  for _ in range(m+1)]
        # for i in range(1,m+1):
        #     dp[i][0] = [dp[i-1][0][0] + nums1[i-1],0]
        #
        # for j in range(1,n+1):
        #     dp[0][j] = [dp[0][j-1][0] + nums2[j-1],1]
        #
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if nums1[i-1] == nums2[j-1]:
        #             dp[i][j] = [dp[i-1][j-1][0] + nums1[i-1],2]
        #         else:
        #             dp[i][j] = max(
        #                 dp[i-1][j],
        #                 dp[i][j-1],
        #                 dp[i-1][j-1] + max(nums1[i-1],nums2[j-1])
        #                            )
        #             if
        # return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.getWinner([1,25,42,35,68,70],2))
    print(s.minSwaps([[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,1]]))
    # print(s.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))
    # print(s.maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100]))