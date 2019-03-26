legal = []
for i in range(10):
    legal.append(str(i))

class Solution:
    def myAtoi(self, str: str) -> int:
        while True:
            if len(str) == 0:
                return 0
            elif str[0] == ' ':
                str=str[1:]
            else:
                break
        
        if str[0] == '-':
            negtive = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
            negtive = False
        else:
            negtive = False
        
        string = ''
        for s in str:
            if s in legal:
                string += s
            else:
                break
        
        if string == '':
            return 0
        
        if negtive:
            output = -int(string)
        else:
            output = int(string)
        
        if output <= -(2**31):
            return -(2**31)
        elif output >= (2**31)-1:
            return (2**31)-1
        else:
            return output