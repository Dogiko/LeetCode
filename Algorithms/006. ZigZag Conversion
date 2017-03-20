class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            ans = s
        else:
            str_list = []
            for i in range(numRows):
                str_list.append("")
            period = 2 * numRows - 2
            for i in range(len(s)):
                j = i % period
                if j < numRows:
                    str_list[j] += s[i]
                else:
                    str_list[period - j] += s[i]
            
            ans = ""
            for str in str_list:
                ans += str
                
        return ans