class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        suspects_dict = {}
        for i in range(len(nums)):
            if nums[i] not in suspects_dict:
                suspects_dict[target - nums[i]] = i
            else:
                p1 = suspects_dict[nums[i]]
                p2 = i
                break
            
        return [p1, p2]

"""
use suspects_dict to record "suspects" and relate index

--
Intuitively solution may be:
for nums[0], review nums[1] ~ nums[n]
for nums[1], review nums[2] ~ nums[n]
......
this way must slower then O(n)
--
"""