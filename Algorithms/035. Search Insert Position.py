class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        output = 0
        while len(nums) > 0:
            half_cut = int((len(nums)-1)/2)
            if nums[half_cut]<target:
                output += half_cut+1
                nums = nums[half_cut+1:]
            else:
                nums = nums[:half_cut]
        
        return output