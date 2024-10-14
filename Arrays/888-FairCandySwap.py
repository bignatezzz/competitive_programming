class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        a = set()
        for i in aliceSizes:
            a.add(i)
        
        for j in bobSizes:
            if (j - (sumB - sumA)//2 in a):
                return [j -(sumB- sumA)//2, j]

      #  for a in aliceSizes:
     #       for b in bobSizes:
      #          if((sumB - sumA)//2 == b - a):
        #            return [a,b]
