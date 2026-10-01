class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)

        if len(hand) % groupSize != 0:
            return False

        used_dict = {} 
        # card_dict = {}
        # for card in hand:
        #     card_dict[card] = card_dict.get(card,0) + 1
    

        for card in hand:

            if card - 1 in used_dict and len(used_dict[card - 1])> 0:
                curr_len = used_dict[card - 1].pop() + 1
            else:
                curr_len = 1

            if curr_len < groupSize:
                if card not in used_dict:
                    used_dict[card] = []     
                used_dict[card].append(curr_len)
        
        
        for lengths in used_dict.values():
            if len(lengths) >0:
                return False
        
        return True




        
    

            
    




        