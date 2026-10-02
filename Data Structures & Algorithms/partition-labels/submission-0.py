class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        search = set()
        count = {}
        res = []
        for char in s:
            count[char] = count.get(char, 0) + 1
        

        
        curr_len = 0
        
        for char in s:

            search.add(char)
            curr_len += 1

            if count[char] == 1 and len(search) == 1:
                res.append(curr_len)
                curr_len = 0
            
            count[char] -= 1

            if count[char] == 0:
                search.remove(char)

            
        return res



            

            


        
        

        