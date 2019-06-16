from typing import *

import re

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        num = min(A)
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10
        return 1 if s % 2 == 0 else 0

    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        stumap = {}
        for item in items:
            if not stumap.__contains__(item[0]):
                stumap[item[0]] = []
            if len(stumap[item[0]]) < 5:
                stumap[item[0]].append(item[1])
            else:
                stumap[item[0]].sort(reverse=True)
                if item[1] > stumap[item[0]][-1]:
                    stumap[item[0]][-1] = item[1]
        ans = [[key,sum(value)//len(value)] for key,value in stumap.items()]
        ans.sort(key=lambda x:x[0])
        return ans
    def permute(self, S: str) -> List[str]:
        sp = re.split('[{}]',S)
        while True:
            try:
                sp.remove('')
            except:
                break
        for i in range(len(sp)):
            sp[i] = sp[i].split(',')

            # if len(emu) == 1:
            #     sp[i] = emu
            # else:
            #     new = emu.copy()
            #     res = emu.copy()
            #     l = len(emu)
            #     for j in range(1,l):
            #         last = new.copy()
            #         new = []
            #         for le in last:
            #             for ae in emu:
            #                 if ae > le[-1]:
            #                     new.append(le+ae)
            #         res += new
            #     res.sort()
            #     sp[i] = res
        ans = []
        maxdeep = len(sp)
        def go(last:str,deep:int):
            if deep == maxdeep:
                ans.append(last)
                return
            for it in sp[deep]:
                go(last+it,deep+1)
        go('',0)
        return sorted(ans)

    def confusingNumberII(self, N: int) -> int:
        strN = str(int(N))
        if int(strN[1:]) == 0 and strN[0] == '1':
            bias = 1
        else:
            bias = 0
        numofN = len(strN) - bias
        base = '0,1,6,8,9'.split(',')
        temp = []
        def go(last:str,deep:int):
            if deep == numofN:
                temp.append(last)
                return
            for it in base:
                go(last+it,deep+1)
        go('',0)
        ans = []
        for t in temp:
            num = int(t)
            if 1 < num <= N:
                s = str(num)[::-1]
                s = s.replace('6','a')
                s = s.replace('9','6')
                s = s.replace('a','9')
                if int(s) != num:
                    ans.append(num)
        return len(ans) + bias

    def confusingNumberII2(self, N: int) -> int:
        strN = str(int(N))
        if int(strN[1:]) == 0 and strN[0] == '1':
            bias = 1
        else:
            bias = 0
        numofN = len(strN) - bias
        base = '0,1,6,8,9'.split(',')
        temp = []
        def go(last:str,deep:int,bias:int):
            if deep == numofN:
                temp.append(last)
                return bias
            val = int(last+'0'*(numofN-deep))
            val9 = int(last+'9'*(numofN-deep))
            if val > N:
                return bias
            if val9 <= N and deep > 0:
                dns = str(int(last))
                done_num = len(dns)
                remain = numofN - deep
                if done_num > remain:
                    pos = remain
                    flag = False
                    if (dns[-1] == '6') :
                        if dns[pos] != '9':
                            flag = True
                    elif (dns[-1] == '9') :
                        if dns[pos] != '6':
                            flag = True
                    elif dns[-1] != dns[pos]:
                        flag = True
                    if flag:
                        bias += 5 ** remain
                        return bias
            for it in base:
                bias = go(last+it,deep+1,bias)
            return bias
        bias = go('',0,bias)
        ans = 0
        for t in temp:
            num = int(t)
            if 1 < num <= N:
                ss = str(num)
                flag = False
                if len(ss) % 2 == 1 and (ss[len(ss) // 2] == '6' or ss[len(ss) // 2] == '9'):
                    ans += 1
                    continue
                for i in range(len(ss) // 2):
                    if ss[i] == '6':
                        if ss[-i-1] != '9':
                            flag = True
                            break
                    elif ss[i] == '9':
                        if ss[-i-1] != '6':
                            flag = True
                            break
                    else:
                        if ss[i] != ss[-i-1]:
                            flag=True
                            break
                if flag:
                    ans += 1
        return ans + bias
if __name__ == '__main__':
    s = Solution()
    # print(s.permute("{a,b}c{d,e}f"))
    # print(s.confusingNumberII(1e9))
    print(s.confusingNumberII2(1e9))