class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #set up correct array
        s1_arr = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            s1_arr[index] += 1
        

        starting_window = s2[0: len(s1)]
        
        check_arr = [0] * 26
        for char in starting_window:
            index = ord(char) - ord('a')
            check_arr[index] += 1
        
        window_left = 0
        window_right = len(s1)

        while window_right < len(s2):
            if check_arr == s1_arr:
                return True
            else:
                # Remove the character at window_left from the count
                first_index = ord(s2[window_left]) - ord('a')
                check_arr[first_index] -= 1
                window_left += 1

                # Add the character at window_right to the count
                last_index = ord(s2[window_right]) - ord('a')
                check_arr[last_index] += 1
                window_right += 1
        
        return check_arr == s1_arr
        



        