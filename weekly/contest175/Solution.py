from typing import *
import time


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ds = set()
        if arr.count(0) > 1:
            return True
        for a in arr:
            if a % 2 == 0 and a != 0:
                ds.add(a)
        if len(ds) == 0:
            return False
        for a in arr:
            if 2 * a in ds:
                return True

    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        ans = 0
        for k,v in cs.items():
            ans += max(0, v - ct[k])
        return ans

    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        ans = [0]
        dirs = [(-1,-1),(-1,1),(0,-1)]
        maxseats = [[0]*n for _ in range(m)]
        if seats[-1][-1] == '.':
            maxseats[-1][-1] = 1
        for i in range(m)[::-1]:
            if i < m -1:
                maxseats[i][-1] = maxseats[i+1][0]
                if seats[i][-1] == '.':
                    maxseats[i][-1] += 1
            for j in range(n-1)[::-1]:
                maxseats[i][j] = maxseats[i][j+1]
                if seats[i][j] == '.':
                    maxseats[i][j] += 1

        def dfs(i,j,v,s:set):
            if j >= n:
                j = 0
                i += 1
            if i >= m:
                ans[0] = max(ans[0],v)
                return
            if seats[i][j] == '#':
                dfs(i,j+1,v,s)
                return
            if v + maxseats[i][j] < ans[0]:
                return
            flag1 = True
            for d in dirs:
                ii = i + d[0]
                jj = j + d[1]
                if ii >= 0 and 0 <= jj < n:
                    if seats[ii][jj] == '.' and (ii,jj) in s:
                        flag1 = False
                        break
            if flag1:
                # ss = copy.deepcopy(s)
                ss = s.copy()
                ss.add((i,j))
                dfs(i,j+2,v+1,ss)
            dfs(i, j + 1, v, s)

        dfs(0,0,0,set())
        return ans[0]



class TweetCounts:

    def __init__(self):
        self.user_record = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.user_record:
            self.user_record[tweetName] = [time]
        else:
            for i,item in enumerate(self.user_record[tweetName]):
                if item > time:
                    self.user_record[tweetName].insert(i,time)
                    return
            self.user_record[tweetName].append(time)




    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        parm = {'minute':60,'hour':60*60,'day':60*60*24}
        fr = parm[freq]
        record = self.user_record[tweetName]
        n = (endTime - startTime + 1 - 1) // fr + 1
        ans = [0] * n
        for t in record:
            if t < startTime:
                continue
            if t > endTime:
                break
            pos = (t - startTime) // fr
            ans[pos] += 1
        return ans




if __name__ == '__main__':
    # s = Solution()
    # print(s.minSteps(s = "bab", t = "aba"))
    # print(s.minSteps(s = "leetcode", t = "practice"))
    # print(s.minSteps(s = "anagram", t = "mangaar"))
    # print(s.minSteps(s = "xxyyzz", t = "xxyyzz"))
    # print(s.minSteps(s = "friend", t = "family"))
    # s = TweetCounts()
    # s.recordTweet("tweet3", 0)
    # s.recordTweet("tweet3", 60)
    # s.recordTweet("tweet3", 10)
    # print(s.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))
    # print(s.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))
    # s.recordTweet("tweet3", 120)
    # print(s.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))
    s = Solution()
    # print(s.maxStudents([["#",".","#","#",".","#"],
    #           [".","#","#","#","#","."],
    #           ["#",".","#","#",".","#"]]))
    # print(s.maxStudents([[".","#"],
    #           ["#","#"],
    #           ["#","."],
    #           ["#","#"],
    #           [".","#"]]))
    # print(s.maxStudents([["#",".",".",".","#"],
    #           [".","#",".","#","."],
    #           [".",".","#",".","."],
    #           [".","#",".","#","."],
    #           ["#",".",".",".","#"]]))
    st = time.time()
    print(s.maxStudents([[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]]))
    print(st - time.time())