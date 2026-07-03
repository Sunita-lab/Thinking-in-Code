class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        i = 0
        while i < len(bills):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                if fives > 0:
                    fives -= 1
                else:
                    return False
                tens += 1
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
            i += 1        
        return True                                    
        