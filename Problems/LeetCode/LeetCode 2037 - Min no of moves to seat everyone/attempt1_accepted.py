class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        i = 0
        while i < len(seats):
            moves += abs(seats[i] - students[i])
            i += 1
        return moves    