class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left1 = mid
                right1 = mid
                for i in range (mid-1, -1, -1):
                    if nums[i] == target:
                        left1 -= 1
                    else:
                        break    
                for i in range (mid+1, len(nums)):
                    if nums[i] == target:
                        right1 += 1
                    else:
                        break    
                return [left1,right1]    
        return [-1,-1]                   



        