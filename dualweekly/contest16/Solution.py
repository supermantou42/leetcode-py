from typing import *
import time

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mmax = arr[-1]
        for i in range(len(arr)-1)[::-1]:
            t = arr[i]
            arr[i] = mmax
            mmax = max(mmax, t)
        arr[-1] = -1
        return arr

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        total = sum(arr)
        n = len(arr)
        if total <= target:
            return arr[0]
        if n * arr[-1] >= target:
            return int(target / n + 0.5)
        remain = arr.copy()
        for i in range(n-1)[::-1]:
            remain[i] += remain[i+1]
        l = 0
        r = n
        mid = 0
        t = 0
        while l < r:
            mid = (l+r)//2
            t = arr[mid] * (mid) + remain[mid]
            if t == target:
                return arr[mid]
            if t > target:
                l = mid + 1
            else:
                r = mid
        t =  arr[l] * (l) + remain[l]
        gap1 = (target - t) % (l)
        a1 = arr[l] + (target - t) // l
        a2 = a1 + 1
        gap2 = a2 * l + remain[l] - target
        if gap1 <= gap2:
            return a1
        else:
            return a2

    def deepestLeavesSum(self, root: TreeNode) -> int:
        import queue
        q = queue.Queue()
        q.put_nowait(root)
        while not q.empty():
            total = 0
            for _ in range(q.qsize()):
                node = q.get_nowait()
                total += node.val
                if node.left is not None:
                    q.put_nowait(node.left)
                if node.right is not None:
                    q.put_nowait(node.right)
            if q.qsize() == 0:
                return total

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        n = len(board[0])
        direction = [(-1, 0), (-1, -1), (0, -1)]
        board = list(map(list,board))
        board[-1][-1] = '0'
        dp = [[[0,1] for _ in range(n)] for _ in range(m)]
        for j in range(1,n):
            if board[0][j] == 'X' or dp[0][j-1][0] == -1:
                dp[0][j] = [-1,-1]
            else:
                dp[0][j] = [dp[0][j-1][0] + int(board[0][j]),1]
        for i in range(1,m):
            if board[i][0] == 'X' or dp[i-1][0][0] == -1:
                dp[i][0] = [-1,-1]
            else:
                dp[i][0] = [dp[i-1][0][0] + int(board[i][0]),1]
        for i in range(1,m):
            for j in range(1,n):
                if board[i][j] == 'X':
                    dp[i][j] = [-1,-1]
                else:
                    v = []
                    t = []
                    me = int(board[i][j])
                    for d in direction:
                        xx = i + d[0]
                        yy = j + d[1]
                        if xx >=0 and yy >= 0:
                            if dp[xx][yy][0] == -1:
                                continue
                            v.append(dp[xx][yy][0] + me)
                            t.append(dp[xx][yy][1])
                    if len(v) == 0:
                        dp[i][j] = [-1,-1]
                    else:
                        ma = max(v)
                        tt = 0
                        for k in range(len(v)):
                            if v[k] == ma:
                                tt+=t[k]
                        dp[i][j] = [ma,tt]
        ans = dp[-1][-1]
        if ans == [-1,-1]:
            return [0,0]
        else:
            ans[0] = ans[0] % (10**9 +7)
            ans[1] = ans[1] % (10**9 +7)
            return ans


        # direction = [(-1,0),(-1,-1),(0,-1)]
        # best = [0, 0]
        # def go(x,y,score):
        #     if board[x][y] == 'X':
        #         return
        #     if board[x][y] == 'E':
        #         if score > best[0]:
        #             best[0] = score
        #             best[1] = 1
        #         elif score == best[0]:
        #             best[1] += 1
        #         return
        #     score += int(board[x][y])
        #     for d in direction:
        #         xx = x + d[0]
        #         yy = y + d[1]
        #         if xx >=0 and yy >= 0:
        #             go(xx,yy,score)
        # go(m-1,n-1,0)
        # return best


if __name__ == '__main__':
    s = Solution()
    # print(s.findBestValue(arr = [4,9,3], target = 10))
    # print(s.findBestValue(arr = [2,3,5], target = 10))
    # print(s.findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))
    # print(s.findBestValue([1547,83230,57084,93444,70879], 71237))
    print(s.pathsWithMaxScore(board = ["E23","2X2","12S"]))
    print(s.pathsWithMaxScore(board = ["E12","1X1","21S"]))
    print(s.pathsWithMaxScore(board = ["E11","XXX","11S"]))
    print(s.pathsWithMaxScore(board = ["EX","XS"]))
    st = time.time()
    # print(s.pathsWithMaxScore(board = ["E4789338X943596124X2676X552X587877X456943458X29735","611684759486631913932337237231351921X2152919376427","4499519117827344997451XX34X46693XX7181343557483669","414951X685152X89829782685X4912581351X3216914721551","X387271851925X3629265X99195X5897581179XX369637813X","1X8X2682518937289551X98X7983XX34993116413343558825","X92X12119593186X675113X682143777XX8981619298251984","X671798198463X5314971262X9392393XXX544537813812728","81856146535454X3678775784456289257XX8221X2488XXX68","77X3592XX94844399282X2X6336122XX7X18244862821X26XX","28885X948512X3585X27824186222X73X9X56441X9X4689517","344X495X682875968X82X9877379XX386748175X6293X44159","1924352186149295919715X27X555626X17798524189528625","3435681879X49727366745492X648X5952772978787143263X","412933788234154913356X2X9X144818X21XX5629259785133","489644765X456XX44XX2X5387637879X662941398337817381","7617826679176XX173173537173164967296764519X3427693","7X69X5466277665871135253486758156766536X5436X16728","318152574426X696X18X833396113X31862234511611X89691","X147492241256344555237X94772X9X5136226469551942X29","X29846X49419853778154XX636X35XX5232391787617416258","8885851X996538X163323347235993741926591X72X1761X14","226X8136988863232963682217521777419144333838517835","3197757518X241117949451X423XX55861XX6161938551X752","49X149355329X617X51X21965452X962X42762X25968X73754","X1176483834957794897816132X5X942366794665183797399","48294674492176X1X663644X58X17729X4482638X92X482422","51X16X157889846864X1436338776687677X44895154219626","782XX82XX432848434721692X55564975938X2649681569663","26792517214X8863X9896XX64619817916123168945761X526","X7XX319393797X184679X421943743279X1486126364341595","11425763X68563511X2496983325426X151456X5X459542989","89872654932254X5525587692326476X65562X59X635129314","6X944371656471737X9673645X4145X821X942995885X86522","64XX328X8243XX3445X6412955X87X42355234X73223243421","944391299X158X962X9X259552884441434XX9349X5XX79855","98422711429356771336494176X56X2584376X2354X72X5416","7135X7X9X3X699929714X61664916968X1896X5X1985386642","22969X77414X2154167176388X3313X918X1558161XX413862","4X141958614412616921588565488847635X837996835937X6","X416X64649X955369739187781488XX77129X6966899351X74","9X2349175X345X7469265842X591X4748167996963X63X7211","3117349374592412365636726147X52469X8921X1888159627","254513X73629359514989286822X7X89391797X357546X9145","8882877128738295914941X56995X243888XX595873XX99217","X947591X382X19613453263544415821689719794546655278","51X4565271954965486X492693X731844471486X149X7166X5","731X1816268181645946X2123376981X13X834338226X28X36","6X72X3599546159X378191718821X746789239488712584143","5982153336X61729X66339596838X77751396645929982913S"]))
    print(time.time() - st)