from typing import *
import time


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        nn = bin(num)[2:]
        return len(nn) + nn.count('1') - 1


    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        prev = sum(arr[:k])
        ans = 0
        if prev >= threshold:
            ans += 1
        for i in range(k,len(arr)):
            prev = prev +arr[i] - arr[i-k]
            if prev >= threshold:
                ans += 1
        return ans
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        ang = abs(5*hour + minutes / 12 - minutes) * 6
        if ang>=180:
            ang = 360 - ang
        elif ang < 0:
            ang = -ang
        return ang
    def minJumps(self, arr: List[int]) -> int:
        indexmap = {arr[0]:[0]}
        n = len(arr)

        for i in range(n):
            if arr[i] not in indexmap:
                indexmap[arr[i]] = []
            if i > 0 and arr[i] == arr[i-1]:
                indexmap[arr[i]] = indexmap[arr[i]][:-1]
            indexmap[arr[i]].append(i)
        if n == len(indexmap):
            return n - 1

        i = 0
        import queue
        q = queue.Queue()
        q.put_nowait(0)
        visited = set()
        visited.add(0)
        while q.qsize() > 0:
            for j in range(q.qsize()):
                now = q.get_nowait()
                if now == n - 1:
                    return i
                visited.add(now)
                l = now-1
                r = now+1
                if l >= 0 and l not in visited:
                    q.put_nowait(l)
                if r < n and r not in visited:
                    q.put_nowait(r)
                for a in indexmap[arr[now]]:
                    if a not in visited:
                        q.put_nowait(a)
            i += 1
        return n - 1




if __name__ == '__main__':
    s = Solution()
    # print(s.angleClock(12,30))
    # print(s.angleClock(3,30))
    # print(s.angleClock(3,15))
    # print(s.angleClock(4,50))
    # print(s.angleClock(12,0))
    # print(s.angleClock(1,57))
    # print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
    # print(s.minJumps([7]))
    # print(s.minJumps([7,6,9,6,9,6,9,7]))
    # print(s.minJumps([6,1,9]))
    # print(s.minJumps([11,22,7,7,7,7,7,7,7,22,13]))
    st =time.time()
    print(s.minJumps([7]*(5*10**4)+[11]))
    print(time.time() - st)