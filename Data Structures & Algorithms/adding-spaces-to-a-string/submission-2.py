class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        curr_space = 0
        new_str = []

        curr_word = ""
        for i in range(len(s)):
            if curr_space < len(spaces) and i == spaces[curr_space]:
                new_str.append(curr_word)
                curr_word = ""
                curr_space += 1
            curr_word += s[i]
        
        new_str.append(curr_word)     
        return " ".join(new_str)

