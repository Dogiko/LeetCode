class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        odd_ans = ""
        for i in range(len(s)):
            for j in range(0, min(i+1, len(s) - i)):
                if s[i - j] != s[i + j]:
                    if len(odd_ans) < (2*j ):
                        odd_ans = s[i - j + 1:i + j]
                    break
                
                if (j == (len(s) - i - 1)) or (j == i):
                    if len(odd_ans) < (2*j + 2):
                        odd_ans = s[i - j :i + j + 1]
        
        even_ans = ""
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                for j in range(0, min(i+1, len(s) - i - 1)):
                    if s[i - j] != s[i + j +1]:
                        if len(even_ans) < (2*j + 1):
                            even_ans = s[i - j + 1:i + j + 1]
                        break
                    
                    if (j == (len(s) - i - 2)) or (j == i):
                        if len(even_ans) < (2*j + 3):
                            even_ans = s[i - j :i + j + 2]
        
        if len(odd_ans) > len(even_ans):
            ans = odd_ans
        else:
            ans = even_ans

        return ans