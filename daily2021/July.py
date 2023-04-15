from typing import *
import time


class Solution:

    #5th
    def countOfAtoms(self, formula: str) -> str:
        def fun(subformula: str):
            d = {}
            tempword = ''
            tempd = {}
            l = len(subformula)
            i = 0
            brck_cnt = 0
            last_idx = -1
            while i < l:
                if subformula[i] == '(':
                    if tempword:
                        d.update()
                    if last_idx == -1:
                        last_idx=i
                    brck_cnt+=1
                    i+=1
                elif subformula[i] == ')':
                    brck_cnt-=1
                    if brck_cnt==0:
                        tempd


