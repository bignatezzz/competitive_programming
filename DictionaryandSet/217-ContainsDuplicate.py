class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count = set()

       

        for num in nums:
            if not num in count:
                count.add(num)
            else:
                return True
            
        return False

        

        
