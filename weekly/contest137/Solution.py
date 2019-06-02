from typing import *
import copy

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 0:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.remove(stones[-1])
                stones.remove(stones[-1])
            else:
                stones[-1] -= stones[-2]
                stones.remove(stones[-2])
        return stones[0] if len(stones) > 0 else 0

    def removeDuplicates(self, S: str) -> str:
        arr = list(S)
        length = len(arr)
        i = 1
        while 0 <= i < length:
            if arr[i] == arr[i - 1]:
                arr.pop(i - 1)
                arr.pop(i - 1)
                length -= 2
                i -= 1
            else:
                i += 1
            if i == 0:
                i = 1
        return "".join(arr)

    def longestStrChain(self, words: List[str]) -> int:
        def isPrev(before, after) -> bool:
            i = 0
            j = 0
            while i < len(before) and j < len(after):
                if before[i] == after[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return j - i <= 1

        words.sort(key=lambda x: len(x))
        m = {}
        for word in words:
            if not m.__contains__(len(word)):
                m[len(word)] = []
            m[len(word)].append(word)
        def go(base) -> int:
            m_temp = copy.deepcopy(m)
            if not m_temp.__contains__(base):
                return 0
            for i in range(base+1, len(words[-1])+1):
                if not m_temp.__contains__(i):
                    return i - 1 - base + 1
                need_remove = []
                for w1 in m_temp[i]:
                    flag = False
                    for w2 in m_temp[i - 1]:
                        if isPrev(w2, w1):
                            flag = True
                            break
                    if not flag:
                        need_remove.append(w1)
                for nr in need_remove:
                    m_temp[i].remove(nr)
                if len(m_temp[i]) == 0:
                    return i - 1 - base + 1
            return len(words[-1]) - base + 1
        total_max = 1
        for base in range(len(words[0]), len(words[-1])):
            if base > len(words[-1]) - total_max:
                break
            now_max = go(base)
            if now_max > total_max:
                total_max = now_max
        return total_max


    def lastStoneWeightII(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.remove(stones[-1])
                stones.remove(stones[-1])
            else:
                stones[-1] -= stones[-2]
                stones.remove(stones[-2])
        return stones[0] if len(stones) > 0 else 0

if __name__ == '__main__':
    s = Solution()
    # 6
    # print(s.longestStrChain(["sgtnz","sgtz","sgz","ikrcyoglz","ajelpkpx","ajelpkpxm","srqgtnz","srqgotnz","srgtnz","ijkrcyoglz"]))
    # 7
    # print(s.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
    # 8
    # print(s.longestStrChain(["msnq","klcbjhjm","znui","gy","msntlq","klcbqjhjm","zi","hwhzjgxzd","whzgxzd","zui","rmnqxy","msntzlq","jri","rbmnqxy","gqvbytgny","xh","wxkhyb","gqvbtgy","ctl","klcbqjhbjm","gbgy","klbh","erbmnqxy","mka","gvbtgy","klcbjhj","klbjh","zlnuci","gqvbytgy","mk","whzjgxzd","bgy","wxkhb","xkh","gvbgy","rmnxy","wxkh","msnlq","ct","hwhhzjgxzd","zlnui","klbjhj","jr","jrvi","rmny"]))
    print(s.lastStoneWeightII([2,7,4,1,8,1]))