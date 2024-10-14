class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]  # The first element is always 1
        for i in range(1, rowIndex + 1):
            # Compute the next element using the binomial coefficient relation
            row.append(row[-1] * (rowIndex - i + 1) // i)
        return row
