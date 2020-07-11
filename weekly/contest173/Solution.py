from typing import *
import time


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == '':
            return 0
        if s == s[::-1] or s.count('a') == 0 or s.count('b') == 0:
            return 1
        return 2

    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int,
                              maxDistance: int) -> List[int]:
        temp = []
        for r in restaurants:
            if r[2] >= veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance:
                temp.append(r)
        temp.sort(key=lambda x:(x[1],x[0]),reverse=True)
        return list(map(lambda x:x[0],temp))

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[distanceThreshold+1] * n for _ in range(n)]
        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        ans = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt +=1
            ans.append(cnt)
        l = min(ans)
        for i in range(n)[::-1]:
            if ans[i] == l:
                return i

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        if n == d:
            return sum(jobDifficulty)
        dp = [[-1]*n for _ in range(d)]
        lastmax = [[-1]*n for _ in range(n)]
        dp[0][0] = jobDifficulty[0]
        lastmax[0][0] = jobDifficulty[0]
        for i in range(n):
            lastmax[i][i] = jobDifficulty[i]

        for i in range(n):
            for j in range(i+1,n):
                lastmax[i][j] = max(lastmax[i][j-1], jobDifficulty[j])

        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])
        for i in range(1,d):
            dp[i][i] = dp[i-1][i-1] + jobDifficulty[i]
        for i in range(1,d):
            for j in range(i+1,n):
                dm = 10**9
                for k in range(i-1,j):
                    dk = dp[i-1][k] + lastmax[k+1][j] # max(jobDifficulty[k+1:j+1])
                    dm = min(dk,dm)
                dp[i][j] = dm
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
    # print(s.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))
    # print(s.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))
    # print(s.minDifficulty(jobDifficulty = [9,9,9], d = 4))
    # print(s.minDifficulty(jobDifficulty = [1,1,1], d = 3))
    # print(s.minDifficulty(jobDifficulty = [7,1,7,1,7,1], d = 3))
    # print(s.minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6))
    # print(s.minDifficulty([143,446,351,170,117,963,785,76,139,772,452,743,23,767,564,872,922,532,957,945,203,615,843,909,458,320,290,235,174,814,414,669,422,769,781,721,523,94,100,464,484,562,941],5))
    start = time.time()
    print(s.minDifficulty([104,355,542,314,348,9,30,352,224,70,139,49,982,201,78,770,572,649,674,591,904,985,293,435,336,46,930,449,974,174,313,454,94,216,275,662,999,691,115,235,509,519,943,465,883,398,648,846,660,636,111,883,412,898,607,459,352,169,632,688,302,753,246,676,260,851,861,957,943,283,759,137,360,500,51,740,158,333,42,183,629,756,622,992,853,863,841,37,2,71,562,55,0,11,839,439,491,304,543,469,588,143,74,220,461,232,978,394,537,103,663,881,852,111,436,463,794,246,825,857,181,858,597,712,458,41,908,602,669,126,867,417,843,631,978,646,309,628,687,321,733,563,454,342,748,72,566,583,106,513,986,395,923,434,632,909,991,721,74,187,620,44,596,499,567,768,731,572,921,112,982,444,512,177,185,456,900,458,480,7,315,857,940,191,663,862,202,647,390,454,483,366,150,758,678,66,983,786,911,960,747,177,940,936,936,203,461,512,779,958,381,823,417,108,936,626,770,881,407,981,945,320,998,775,662,334,444,684,139,687,879,648,127,216,554,313,305,244,425,190,469,79,171,58,208,898,475,93,395,804,506,706,80,947,611,667,200,465,567,699,551,520,775,22,139,436,726,928,394,316,870,623,343,179],8))
    print(time.time() - start)