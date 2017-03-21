class Solution(object):
    def __init__(self):
        self.char = [
            ["M"],
            ["C", "D"],
            ["X", "L"],
            ["I", "V"]
            ]
        
        self.digi = [[ ], [ ], [ ], [ ]]
        for i in range(4):
            self.digi[i].append("")
            self.digi[i].append(self.char[i][0])
            self.digi[i].append(self.char[i][0] + self.char[i][0])
            self.digi[i].append(self.char[i][0] + self.char[i][0] + self.char[i][0])
            if i > 0:
                self.digi[i].append(self.char[i][0] + self.char[i][1])
                self.digi[i].append(self.char[i][1])
                self.digi[i].append(self.char[i][1] + self.char[i][0])
                self.digi[i].append(self.char[i][1] + self.char[i][0] + self.char[i][0])
                self.digi[i].append(self.char[i][1] + self.char[i][0] + self.char[i][0] + self.char[i][0])
                self.digi[i].append(self.char[i][0] + self.char[i - 1][0])
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_digi = ["", "", "", ""]
        for i in range(3, 0, -1):
            m_1 = s.find(self.char[i][0])
            m_5 = s.find(self.char[i][1])
            if (m_1 == -1) and (m_5 == -1):
                continue
            elif (m_1 > -1) ^ (m_5 > -1):
                min_d = max(m_1, m_5)
            else:
                min_d = min(m_1, m_5)
            
            roman_digi[i] = str(s[min_d:])
            s = s[:min_d]
        
        roman_digi[0] = str(s)
        ans = ""
        for i in range(4):
            if roman_digi[i] != "":
                ans += str(self.digi[i].index(roman_digi[i]))
            else:
                ans += "0"
        
        return int(ans)