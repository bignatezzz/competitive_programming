class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dic = {}
        def predict(nums, l, r):
            if(r < l):
                return 0
            key = 100*l + r
            if (key in dic):
                return dic[key]

            


            dic[key] = max(nums[l]-predict(nums,l+1,r), nums[r] - predict(nums,l,r-1))
            return dic[key]

        result = predict(nums,0,len(nums)-1)

        if result >= 0:
            return True
        return False
