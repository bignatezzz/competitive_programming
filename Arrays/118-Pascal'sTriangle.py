class Solution(object):
    def generate(self, numRows):
        lst = [] 
        lst.append([1])
        for i in range(1,numRows):
            tmplist = []
            tmplist.append(1)
            for j in range(i-1):
                tmplist.append(lst[i-1][j]+lst[i-1][j+1])

            tmplist.append(1)
            lst.append(tmplist)
        return lst
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
