from typing import *
import time


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        import collections
        d = collections.Counter([l for l, r in zip(s1, s2) if l != r])
        dx = d['x']
        dy = d['y']
        if (dx + dy) % 2 == 1 or len(s1) != len(s2):
            return -1
        return sum(divmod(dx, 2) + divmod(dy, 2))
