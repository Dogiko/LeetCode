class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_str = ""
        ans = 0
        for c in s:
            if c not in longest_str:
                longest_str +=c
            else:
                ans = max(ans, len(longest_str))
                longest_str = longest_str.split(c)[1] + c
        
        ans = max(ans, len(longest_str))
        return ans