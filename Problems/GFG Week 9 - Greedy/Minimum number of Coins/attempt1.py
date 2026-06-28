class Solution:
    def findMin(self, n):
       # code here 
       
       tens = (n//10)
       n %= 10
       fives = (n//5)
       n %= 5
       twos = (n//2)
       ones = n%2
       return tens +fives + twos + ones