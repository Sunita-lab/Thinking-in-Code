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
                temp = mid
                left1, right1, left2, right2 = 0,mid,mid,len(nums)-1
                while left1 <= right1:
                    mid1 = left1 + (right1 - left1)//2
                    if nums[mid1] != target:
                        left1 = mid1 + 1
                    else:
                        right1 = mid1 - 1    
                while left2 <= right2:
                    mid2 = left2 + (right2-left2)//2
                    if nums[mid2] != target:
                        right2 = mid2 - 1
                    else:
                        left2 = mid2 + 1    
                return [left1,right2]


        return [-1,-1]                   



        