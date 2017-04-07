class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        temp = s.strip().split(" ")
        return len(temp[-1])