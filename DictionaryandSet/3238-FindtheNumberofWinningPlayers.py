class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        dic= {}
        for i in range(n):
            dic[i] = list()
        
        for p in pick:
            dic[p[0]].append(p[1])

        result = 0

        for i in range(n):
            ls = dic[i]
            dic2 = {}
            for l in ls:
                if l in dic2:
                    dic2[l]+=1

                else:
                    dic2[l]=1

                if dic2[l]>i:
                    result += 1

                    break
