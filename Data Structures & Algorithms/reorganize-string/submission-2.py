from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        when it's NOT valid
        - frequency of any number is > half of the string (truncate) + 1  ex.  aaabb 
        - empty string
        
        count the frequencies -> update while using

        determine which letter to use --> largest count
        
        a: 1
        x: 1
        y: 1

        check if one character exceeds

        [heap] -> choose the largest one
        subtract 1 from count

        store: (count, letter)

        aaabb


        if y is still largest count and we just used y, pop -> use next
        '''

        #count letters
        count_dict = defaultdict(int)
        for char in s:
            count_dict[char] += 1
            if count_dict[char] > (len(s) + 1) //2:
                return ""
        
        #put into max heap
        max_heap = []
        for key, value in count_dict.items():
            heapq.heappush(max_heap, (-value, key))
        
        #build new string
        new_str = []
        prev = None
        while max_heap:
            count, char = heapq.heappop(max_heap)
            new_str.append(char)

            if prev:
                heapq.heappush(max_heap, prev)
            
            count += 1
            if count < 0:
                prev = (count, char)
            else:
                prev = None
        
        return "".join(new_str)
        
            
        








        