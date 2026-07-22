class Solution:
    def __init__(self):
        self.current = []
        self.result = []
    def subsets(self, nums: List[int], idx = 0) -> List[List[int]]:
        if idx == len(nums):
            self.result.append(self.current[:])
        else:
            self.current.append(nums[idx])
            self.subsets(nums, idx+1)
            self.current.pop()

            self.subsets(nums, idx+1) 
        return self.result       

        