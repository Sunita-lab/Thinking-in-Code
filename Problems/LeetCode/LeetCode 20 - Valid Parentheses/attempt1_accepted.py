class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        arr = []
        i = 0
        while i < len(s):
            if s[i] in mapping.values():
                arr.append(s[i])
            else:
                if arr and arr[-1] ==  mapping[s[i]] :
                    arr.pop()
                else:
                    return False
            i += 1        
        return True if not arr else False    