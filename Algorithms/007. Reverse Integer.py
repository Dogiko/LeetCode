class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_num = int(str(abs(x))[-1::-1])
        if abs(x) == x:
            if reverse_num < 2**31 -1:
                ans = reverse_num
            else:
                ans = 0
        else:
            if reverse_num <= 2**31 :
                ans = -reverse_num
            else:
                ans = 0
        
        return ans