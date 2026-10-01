class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        max_tank = 0

        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            if (curr_tank + gas[i]) < cost[i]:
                curr_tank = 0
                start = i + 1
                continue

            curr_tank += (gas[i] - cost[i])

            if curr_tank > max_tank:
                max_tank = curr_tank
            
        return start

            

            


