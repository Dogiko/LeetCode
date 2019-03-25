class Solution:
    def isValid(self, s: str) -> bool:
        temp = ""
        for c in s:
            if c==")":
                if temp[-1:]=="(":
                    temp = temp[:-1]
                else:
                    return False
            elif c=="}":
                if temp[-1:]=="{":
                    temp = temp[:-1]
                else:
                    return False
            elif c=="]":
                if temp[-1:]=="[":
                    temp = temp[:-1]
                else:
                    return False
            else:
                temp += c
        
        return temp == ""