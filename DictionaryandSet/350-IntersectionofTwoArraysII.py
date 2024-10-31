class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        unique_intersection = set1.intersection(set2)

        result = []

        for num in unique_intersection:

            count_in_nums1 = nums1.count(num)
            count_in_nums2 = nums2.count(num)

            result.extend([num] * min(count_in_nums1, count_in_nums2))

        return result
    
