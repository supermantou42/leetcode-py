from typing import *
import time

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        return abs((d1 - d2).days)

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        vs = [c for c in leftChild+rightChild if c > -1]
        if len(vs) != n - 1:
            return False
        ss = set(vs)
        if len(ss) != n - 1:
            return False
        return True

    def closestDivisors(self, num: int) -> List[int]:
        import math
        st = math.ceil(math.sqrt(num+2))
        for d in range(1,st+1)[::-1]:
            if (num + 1) % d == 0:
                return [d, (num + 1) // d]
            elif (num + 2) % d == 0:
                return [d, (num + 2) // d]

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dsum = sum(digits)
        if dsum == 0:
            return '0'
        group = [[],[],[]]
        for dd in digits:
            group[dd%3].append(dd)

        if dsum % 3 == 1:
            if len(group[1]) == 0 and len(group[2]) < 2:
                return ''
            if len(group[1]) == 0:
                group[2].sort()
                digits.remove(group[2][0])
                digits.remove(group[2][1])
            else:
                digits.remove(min(group[1]))
        elif dsum % 3 == 2:
            if len(group[2]) == 0 and len(group[1]) < 2:
                return ''
            if len(group[2]) == 0:
                group[1].sort()
                digits.remove(group[1][0])
                digits.remove(group[1][1])
            else:
                digits.remove(min(group[2]))

        n = len(digits)
        if n == 0:
            return ''
        if sum(digits) == 0:
            return '0'
        digits.sort(reverse=True)
        return ''.join(list(map(str,digits)))



if __name__ == '__main__':
    s = Solution()
    # print(s.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
    # print(s.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
    # print(s.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))
    # print(s.validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]))
    # print(s.validateBinaryTreeNodes(n = 4, leftChild = [1,2,3,0], rightChild = [-1,-1,-1,-1]))
    # print(s.closestDivisors(8))
    # print(s.closestDivisors(123))
    # print(s.closestDivisors(999))
    print(s.largestMultipleOfThree([8,1,9]))
    print(s.largestMultipleOfThree([8,6,7,1,0]))
    print(s.largestMultipleOfThree([1]))
    print(s.largestMultipleOfThree([0,0,0,0,0,0]))

