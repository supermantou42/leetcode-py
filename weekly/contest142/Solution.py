from typing import *

class MountainArray:
   def get(self, index: int) -> int:
       return 0
   def length(self) -> int:
       return 10

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        size = len(count)
        max_value = 0
        min_value = 255
        for i in range(size):
            if count[i]>0:
                min_value = i
                break
        for i in range(size)[::-1]:
            if count[i] > 0:
                max_value = i
                break
        total = 0
        total_len = 0
        for i in range(size):
            total += i * count[i]
            total_len += count[i]

        average = total / total_len
        public = count.index(max(count))
        mid_pos = total_len // 2
        mid = 0
        now = 0
        flag = False
        for i in range(len(count)):
            if count[i] == 0:
                continue
            if flag:
                mid = (mid + i) / 2
                break
            now += count[i]
            if now > mid_pos:
                mid = i
                break
            elif now == mid_pos:
                if total_len % 2 != 0:
                    mid = i
                    break
                else:
                    mid = i
                    flag = True
        ans = [min_value, max_value, average, mid, public]
        ans = [float(a) for a in ans]
        return ans

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        plan = [0]*1001
        for s in trips:
            for i in range(s[1],s[2]):
                plan[i] += s[0]
        if max(plan) > capacity:
            return False
        return True

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        pass


    def braceExpansionII(self, expression: str) -> List[str]:
        pattern = []
        def go(subexpression:str):
            if subexpression.count('{') == 0:
                return subexpression.split(',')
            flag = 0
            subsube = []
            last_index = 0
            for i in range(len(subexpression)):
                if subexpression[i] == '{':
                    if flag == 0 and i > last_index:
                        subsube.append(subexpression[last_index:i])
                        last_index = i
                    flag += 1
                if subexpression[i] == '}':
                    flag -= 1
                    if flag == 0:
                        subsube.append(subexpression[last_index:i+1])
                        last_index = i+1
                if flag == 0 and subexpression[i] == ',':
                    subsube.append(',')
                    last_index = i + 1
            subans = []
            for s in subsube:
                if s == ',':
                    subans.append(',')
                    continue
                if s[0] == '{':
                    subans.append(go(s[1:-1]))
                else:
                    subans.append(go(s))
            for i in range(len(subans)):
                if subans[i] == ',':
                    s1 = subans[i-1]
                    s2 = subans[i+1]
                    for s in s1:
                        if s2.count(s) == 0:
                            s2.append(s)
                    subans[i-1] = ''
                    subans[i] = ''
                    subans[i+1] = s2
            while subans.count('') > 0:
                subans.remove('')
            return subans
        op = go(expression)
        ans = set()
        def go2(now:str,deep:int):
            if deep == len(pattern):
                ans.add(now)
                return
            c = pattern[deep]
            for e in c:
                go2(now+e,deep+1)
        go2('',0)
        return list(ans)


if __name__ == '__main__':
    s = Solution()
    # print(s.sampleStats(count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    # print(s.carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11))
    print(s.braceExpansionII("{{a,z}, a{b,c}, {ab,z}}"))