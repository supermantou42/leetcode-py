from typing import *

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        k = len(arr)
        for i in range(len(arr))[::-1]:
            if arr[i] == 0:
                arr.insert(i,0)
        for i in range(len(arr) - k):
            arr.pop(-1)
        print(arr)

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        combied = [(values[i],labels[i]) for i in range(len(values))]
        combied.sort(key=lambda x:x[0],reverse=True)
        remain = {}
        for la in labels:
            remain[la] = use_limit
        cnt = 0
        sum = 0
        for v,l in combied:
            if remain[l] > 0:
                sum+=v
                remain[l] -= 1
                cnt+=1
                if cnt == num_wanted:
                    break
        return sum


    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = [(1,1)]
        rows = len(grid)
        cols = len(grid[0])
        grid = [[1]*cols] + grid + [[1]*cols]
        for i in range(len(grid)):
            grid[i] = [1] + grid[i] + [1]
        pos = [(-1,-1),(-1,0),(-1,1),
               (0,-1),(0,1),
               (1,-1),(1,0),(1,1)]
        # bfs
        deep = 1
        while 1:
            next_queue = []
            while len(queue) > 0:
                q = queue.pop(0)
                for dx,dy in pos:
                    if grid[q[0]+dx][q[1]+dy] == 0:
                        next_queue.append((q[0]+dx,q[1]+dy))
                        grid[q[0] + dx][q[1] + dy] = -deep
            deep += 1
            queue = next_queue
            if len(queue) == 0:
                break

        if grid[-2][-2] >= 0:
            return -1
        else:
            return -grid[-2][-2] + 1

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def go(str1: str, str2: str) -> str:
            l1 = len(str1)
            l2 = len(str2)
            pos = 0
            ml = min(l1,l2)
            for i in range(1,ml+1)[::-1]:
                if str1[:i] == str2[l2-i:]:
                    pos = i
                    break
            if pos == 0:
                return str1+str2
            return str1[:pos]+str2
        s1 = go(str1,str2)
        s2 = go(str2,str1)
        if len(s1) < len(s2):
            return s1
        else:
            return s2



if __name__ == '__main__':
    s = Solution()
    # s.duplicateZeros([1,0,2,3,0,4,5,0])
    # print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(s.shortestCommonSupersequence("atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp",
"xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc"))