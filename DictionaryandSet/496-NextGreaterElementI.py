class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = [None] * len(nums2)  
        top = -1 
        for num in reversed(nums2):
     
            while top >= 0 and stack[top] <= num:
                top -= 1  
            next_greater[num] = stack[top] if top >= 0 else -1
        
            top += 1
            stack[top] = num
    
    
        return [next_greater[num] for num in nums1]
