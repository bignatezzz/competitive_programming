class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(nums, l, r):
            if(r < l):
                return 0

            return max(nums[l]-predict(nums,l+1,r), nums[r] - predict(nums,l,r-1))
     

        result = predict(nums,0,len(nums)-1)

        if result >= 0:
            return True
        return False
