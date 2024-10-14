class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_of_zeros = 0

        for num in nums:
            if num == 0:

                count_of_zeros += 1

            
        while count_of_zeros > 0:
            nums.remove(0)
            nums.append(0)
            count_of_zeros -= 1
        return nums


        
