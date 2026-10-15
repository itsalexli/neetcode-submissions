'''
move = 1 wheel, one slot
0000 start -> string



0000 -> 5555
5000 -> 5 * 4 = 20
5500
5550
5555


invalid: number above and below is inside the digits

'''


from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        dead.add("0000")
        min_time = 0
        
        q = deque(["0000"])

        while q:
            for _ in range(len(q)):
                curr_combo = q.popleft()
                if curr_combo == target:
                        return min_time
                for new_combo in self.generateCombos(curr_combo):
                    if new_combo not in dead:
                        q.append(new_combo)
                        dead.add(new_combo)
            min_time += 1
        return -1



    def generateCombos(self, combo: str) -> List[str]:
        res = []
        for i in range(4):
            up = int(combo[i]) + 1
            if up == 10:
                up = 0
            res.append(combo[:i] + str(up) + combo[i+1:])

            down = int(combo[i]) - 1
            if down == -1:
                down = 9
            res.append(combo[:i] + str(down) + combo[i+1:])
        return res
            
        

        