class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}

        for i in arr:
            if i in dic:
                dic[i] = dic[i] + 1

            else:
                dic[i] = 1

        for j in dic:
            if dic[j] == 1:
                k = k-1
                if k == 0:
                    return j
        
        return ""
            
                
