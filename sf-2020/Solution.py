from typing import *
import time


class Solution:
    def q(self, ) -> str:
        newline = chr(0x0a) + ' '*4
        quotation = chr(0x22)
        s = "class Solution:{0}def q(self, ) -> str: {0}    newline = chr(0x0a) + ' '*4{0}    tab = chr(0x22){0}    s = {1}{2}{1}{0}    s = s.format(newline,quotation,s){0}    return s"
        s = s.format(newline,quotation,s)
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.q())