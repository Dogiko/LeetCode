def left_cut(list_a, list_b, cut_n):
    if len(list_a) == 0:
        return list_b[cut_n:], []
    elif len(list_b) == 0:
        return list_a[cut_n:], []
    else:
        if len(list_a) <= cut_n:
            cut_a = list_a[-1]
        else:
            cut_a = list_a[cut_n-1]

        if len(list_b) <= cut_n:
            cut_b = list_b[-1]
        else:
            cut_b = list_b[cut_n-1]

        if cut_a <= cut_b:
            return list_b, list_a[cut_n:]
        else:
            return list_a, list_b[cut_n:]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        odd = (total_len%2)
        should_be_removed = int((total_len-1)/2)
        currentlly_removed = 0
        while currentlly_removed < should_be_removed:
            cut_n = int((should_be_removed-currentlly_removed +1)/2)
            nums1, nums2 = left_cut(nums1, nums2, cut_n)
            currentlly_removed = total_len - len(nums1) - len(nums2)
        
        candidate = nums1[:2] + nums2[:2]
        candidate.sort()
        if odd:
            return candidate[0]
        else:
            return (candidate[0]+candidate[1])/2