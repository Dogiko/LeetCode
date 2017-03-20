class Solution(object):
    def __init__(self):
        self.char = [
            ["I", "V"],
            ["X", "L"],
            ["C", "D"],
            ["M", ""]
            ]
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        for d in range(4):
            n = int((num % 10**(4 - d)) / 10**(3 - d))
            if n == 0:
                pass
            elif (n > 0) and (n < 4):
                ans += self.char[3 - d][0] * n
            elif n == 4:
                ans += self.char[3 - d][0] + self.char[3 - d][1]
            elif n == 5:
                ans += self.char[3 - d][1]
            elif (n > 5) and (n < 9):
                ans += self.char[3 - d][1] + self.char[3 - d][0] * (n - 5)
            else:
                ans += self.char[3 - d][0] + self.char[4 - d][0]

        return ans