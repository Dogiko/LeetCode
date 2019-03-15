class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        n2letter = {}
        n2letter["2"] = "abc"
        n2letter["3"] = "def"
        n2letter["4"] = "ghi"
        n2letter["5"] = "jkl"
        n2letter["6"] = "mno"
        n2letter["7"] = "pqrs"
        n2letter["8"] = "tuv"
        n2letter["9"] = "wxyz"

        if len(digits)==0:
            return output

        for d in range(len(digits)):
            letters = n2letter[digits[d]]
            if len(output)==0:
                for l in letters:
                    output.append(l)
            else:
                while len(output[0])<=d:
                    for l in letters:
                        output.append(output[0]+l)

                    output.remove(output[0])

        return output