class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if len(arr) < k:
            return []
        diff_arr = []
        for num in arr:
            diff_arr.append(abs(x - num))
        
        smallest = float("inf")
        curr_sum = 0
        for i in range(k):
            curr_sum += arr[i]
        
        left, right = 0, k
        return_arr = arr[left:right]
        smallest = curr_sum

        while right < len(arr):

            curr_sum -= diff_arr[left]
            left += 1
            curr_sum += diff_arr[right]
            right += 1
            
            if curr_sum < smallest:
                smallest = curr_sum
                return_arr = arr[left:right]

            
        
        return return_arr





        


        

        
        


