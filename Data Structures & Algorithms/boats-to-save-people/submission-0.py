class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        #what if person larger?

        #1,3,2,3,2
        #1, 1, 1,  2,2,3,3

        people.sort()
        l, r = 0, len(people) - 1
        min_boats = 0
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
            min_boats += 1
            r -= 1
        
        return min_boats 


            


        